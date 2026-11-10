# Shared park source provenance

Snapshot: proposed shared-source repair, 2026-11-10. These source PRs are
unmerged at this update; this record does not claim shared-main landing or
fleet installation.

- Repository: [opensoft/openBenches](https://github.com/opensoft/openBenches)
- Source commit: [0ac1aa4411669ebf78a62445b953a1d81b8180d4](https://github.com/opensoft/openBenches/commit/0ac1aa4411669ebf78a62445b953a1d81b8180d4)
- Governed change: `openspec/changes/fix-park-handoff-integrity/`
- Sole implementation feature: `specs/177-park-handoff-safety/`
- SET-01: [PR #310](https://github.com/opensoft/openBenches/pull/310), all-leg repository/branch preflight.
- SET-02: [PR #311](https://github.com/opensoft/openBenches/pull/311), preserving unselected records.
- SET-03: [PR #312](https://github.com/opensoft/openBenches/pull/312), verifying origin before accepting an existing resumed worktree.
- SET-04: [PR #313](https://github.com/opensoft/openBenches/pull/313), retrying pending manifest publication independently of content changes and refusing exhausted push attempts.

The following copies are byte-identical to that source commit. Target paths
are relative to this assembly root; source paths are relative to openBenches.

| Target | Source | SHA-256 |
| --- | --- | --- |
| `.specify/extensions/git/scripts/bash/park.sh` | `devBenches/base-image/files/speckit-worktree/templates/specify/extensions/git/scripts/bash/park.sh` | `1ff1e60fc0a4177f69738c3354d571fe3e21d3e1e5d04f8ae7123d8d11d2eed9` |
| `.specify/extensions/git/scripts/bash/resume.sh` | `devBenches/base-image/files/speckit-worktree/templates/specify/extensions/git/scripts/bash/resume.sh` | `624a079255c6ea60b13bbc05d5149fb68b7dafcb4b885268f525316a38c15c0b` |
| `.specify/extensions/git/scripts/bash/workspace-common.sh` | `devBenches/base-image/files/speckit-worktree/templates/specify/extensions/git/scripts/bash/workspace-common.sh` | `f06c0ea12968065434f924c8927039a50e29ff4f453d55b39b3283cc1e499273` |
| `tests/runtime_tooling/test_park_handoff.py` | `devBenches/devcontainer.test/test-speckit-park-handoff.py` | `47b7affc8d214fb3d75ac95e64e87ca77a60c0bdf98274e7350d2b50afd7dceb` |

The shared git-common dependency also compared unchanged against this
candidate before copying. The earlier core-creation correction remains a
declared local deviation in runtime-development.md. The shared resume copy
now supersedes the earlier local failed-fetch correction as well as fixing
the existing-worktree bypass. No content marker is fabricated for this
composite tooling tree, and no shape digest or product/leg pin is changed.

The source tests use only disposable local repositories and bare origins.
They run in this consumer against its own copied tooling without upstream
network reads. The test module's default path resolves this root's .specify
directory. Existing creation/resume tests remain in the same suite.
