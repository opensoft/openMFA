"""Offline regression fixtures for project-local bootstrap corrections."""
import json
import os
from pathlib import Path
import shutil
import subprocess

import pytest

ROOT=Path(__file__).resolve().parents[2]
CORE=Path(".specify/scripts/bash")
EXT=Path(".specify/extensions/git/scripts/bash")


def run(cwd,*args,check=True,env=None):
    clean={k:v for k,v in os.environ.items()
           if not k.startswith(("SPECIFY_","SPECKIT_","AGENT_PROTOCOL_ROOT"))}
    clean.update(GIT_CONFIG_NOSYSTEM="1",GIT_CONFIG_GLOBAL=os.devnull,
                 GIT_TERMINAL_PROMPT="0")
    if env:clean.update(env)
    result=subprocess.run(args,cwd=cwd,env=clean,text=True,capture_output=True,timeout=30)
    if check:
        assert result.returncode==0,result.stdout+result.stderr
    return result


def git(cwd,*args):
    return run(cwd,"git","-c","commit.gpgsign=false",*args).stdout.strip()


def init(path):
    path.mkdir(parents=True)
    git(path,"init","-q","-b","main")
    git(path,"config","user.name","Tooling fixture")
    git(path,"config","user.email","tooling@example.invalid")
    (path/"README.md").write_text("fixture\n")
    git(path,"add","README.md")
    git(path,"commit","-qm","fixture")
    return path


def copy_scripts(repo,folder,names):
    target=repo/folder
    target.mkdir(parents=True,exist_ok=True)
    for name in names:
        shutil.copyfile(ROOT/folder/name,target/name)


@pytest.mark.parametrize("selection",["environment","selector"])
def test_core_spec_creation_preserves_the_paired_worktree_and_selector(tmp_path,selection):
    repo=init(tmp_path/"assembly with spaces")
    copy_scripts(repo,CORE,["common.sh","create-new-feature.sh","setup-plan.sh"])
    templates=repo/".specify/templates"
    templates.mkdir()
    (templates/"spec-template.md").write_text("# fixture spec\n")
    (templates/"plan-template.md").write_text("# fixture plan\n")
    spec=init(repo/"spec")
    branch="009-selected-feature"
    paired=repo/"worktrees"/branch/"spec"
    git(spec,"worktree","add","-b",branch,str(paired))
    directory=Path("worktrees")/branch/"spec/specs"/branch
    (repo/directory).mkdir(parents=True)
    selector=repo/".specify/feature.json"
    original=json.dumps({"feature_directory":str(directory),"fixture_marker":"preserve"})
    selector.write_text(original)
    env={}
    if selection=="environment":
        env={"SPECIFY_FEATURE":branch,"SPECIFY_FEATURE_DIRECTORY":str(directory)}
    preview=run(repo,"bash",str(CORE/"create-new-feature.sh"),"--json","--dry-run",
                "Preview the selected feature",env=env)
    assert Path(json.loads(preview.stdout)["SPEC_FILE"])==repo/directory/"spec.md"
    assert selector.read_text()==original
    assert not (repo/directory/"spec.md").exists()
    assert not (repo/"specs").exists()
    result=run(repo,"bash",str(CORE/"create-new-feature.sh"),"--json",
               "--short-name","different-description","Specify the selected feature",env=env)
    output=json.loads(result.stdout)
    assert output["BRANCH_NAME"]==branch
    assert Path(output["SPEC_FILE"])==repo/directory/"spec.md"
    assert (repo/directory/"spec.md").read_text()=="# fixture spec\n"
    assert selector.read_text()==original
    assert not (repo/"specs").exists()
    plan=run(repo,"bash",str(CORE/"setup-plan.sh"),"--json",env=env)
    assert Path(json.loads(plan.stdout)["IMPL_PLAN"])==repo/directory/"plan.md"
    assert (repo/directory/"plan.md").is_file()
    assert git(paired,"status","--porcelain").startswith("?? specs/")


def test_unselected_single_repository_still_creates_a_new_feature(tmp_path):
    repo=init(tmp_path/"single")
    copy_scripts(repo,CORE,["common.sh","create-new-feature.sh"])
    templates=repo/".specify/templates"
    templates.mkdir()
    (templates/"spec-template.md").write_text("# fixture spec\n")
    result=run(repo,"bash",str(CORE/"create-new-feature.sh"),"--json",
               "--short-name","new-feature","Create a fresh feature")
    assert json.loads(result.stdout)["BRANCH_NAME"]=="001-new-feature"
    assert (repo/"specs/001-new-feature/spec.md").is_file()


@pytest.mark.parametrize("remote_state",["deleted","unavailable","present"])
def test_resume_checks_remote_before_recreating_from_a_cached_ref(tmp_path,remote_state):
    repo=init(tmp_path/"fixture")
    copy_scripts(repo,EXT,["git-common.sh","workspace-common.sh","resume.sh"])
    config=repo/".specify/extensions/git/git-config.yml"
    config.write_text("checkout_mode: worktree\nbase_branch: main\nworktree_root: ../fixture-worktrees\n")
    git(repo,"add",".specify")
    git(repo,"commit","-qm","fixture tooling")
    origin=tmp_path/"fixture-origin.git"
    git(tmp_path,"init","--bare","-q",str(origin))
    git(repo,"remote","add","origin",str(origin))
    branch="001-parked"
    git(repo,"push","-q","origin","HEAD:refs/heads/"+branch)
    git(repo,"fetch","-q","origin")
    parked=git(repo,"rev-parse","HEAD")
    assert git(repo,"rev-parse","refs/remotes/origin/"+branch)==parked
    if remote_state=="deleted":
        git(origin,"update-ref","-d","refs/heads/"+branch)
    elif remote_state=="unavailable":
        git(repo,"remote","set-url","origin",str(tmp_path/"absent-origin.git"))
    workspace=init(tmp_path/"workspace")
    manifests=workspace/"workspaces/local"
    manifests.mkdir(parents=True)
    manifest=manifests/"fixture.yaml"
    manifest.write_text(
        "version: 1\nprojects:\n  - id: fixture\n    shape: single\n"
        "    tracking_branch: main\n    worktree_root: ../fixture-worktrees\n"
        "    parked_at: 2026-11-10T00:00:00Z\n    parked_on: fixture\n"
        "    features:\n      - branch: "+branch+"\n        legs:\n"
        "          - role: repo\n            parked_commit: "+parked+"\n"
        "            wip: false\n            wip_depth: 0\n            pushed: true\n")
    before=manifest.read_bytes()
    result=run(repo,"bash",str(EXT/"resume.sh"),"--json","--workspace",str(workspace),
               env={"AGENT_PROTOCOL_ROOT":str(tmp_path/"isolated-protocol")},check=False)
    tree=tmp_path/"fixture-worktrees"/branch
    if remote_state=="present":
        assert result.returncode==0,result.stdout+result.stderr
        assert git(tree,"rev-parse","HEAD")==parked
    else:
        assert result.returncode==2,result.stdout+result.stderr
        assert "could not be verified" in result.stderr
        assert not tree.exists()
        assert git(repo,"rev-parse","refs/remotes/origin/"+branch)==parked
    assert manifest.read_bytes()==before
