# Shared park source provenance

Snapshot: proposed shared-source repair, 2026-11-10. These source PRs are
unmerged at this update; this record does not claim shared-main landing or
fleet installation.

- Repository: [opensoft/openBenches](https://github.com/opensoft/openBenches)
- Source commit: [9ec3e7ca686d5a92db64ddfe24b1467c1bae75f7](https://github.com/opensoft/openBenches/commit/9ec3e7ca686d5a92db64ddfe24b1467c1bae75f7)
- Governed change: `openspec/changes/fix-park-handoff-integrity/`
- Sole implementation feature: `specs/177-park-handoff-safety/`
- SET-01: [PR #310](https://github.com/opensoft/openBenches/pull/310), all-leg repository/branch preflight.
- SET-02: [PR #311](https://github.com/opensoft/openBenches/pull/311), preserving unselected records.

The following copies are byte-identical to that source commit. Target paths
are relative to this assembly root; source paths are relative to openBenches.

| Target | Source | SHA-256 |
| --- | --- | --- |
| `.specify/extensions/git/scripts/bash/park.sh` | `devBenches/base-image/files/speckit-worktree/templates/specify/extensions/git/scripts/bash/park.sh` | `213d5d0aaf2f74662e2e149aaf71e8c70845eed376ca35677454a1bbb4814cda` |
| `.specify/extensions/git/scripts/bash/workspace-common.sh` | `devBenches/base-image/files/speckit-worktree/templates/specify/extensions/git/scripts/bash/workspace-common.sh` | `6eed63625180f361c3ebee463d09f1ef8704d9e761cec51e7ea50e1a0337b489` |
| `tests/runtime_tooling/test_park_handoff.py` | `devBenches/devcontainer.test/test-speckit-park-handoff.py` | `1ec9550332bf406462241be4315b7d754c71ddcfb208e04ace1e10c71201f249` |

The shared git-common dependency also compared unchanged against this
candidate before copying. The earlier local core-creation and resume fixes
remain declared in runtime-development.md; they are not misrepresented as
shared upstream changes. No content marker is fabricated for this composite
tooling tree, and no shape digest or product/leg pin is changed.

The source tests use only disposable local repositories and bare origins.
They run in this consumer against its own copied tooling without upstream
network reads. The test module's default path resolves this root's .specify
directory. Existing creation/resume tests remain in the same suite.
