# Shared park source provenance

Snapshot: proposed shared-source repair, 2026-11-10. These source PRs are
unmerged at this update; this record does not claim shared-main landing or
fleet installation.

- Repository: [opensoft/openBenches](https://github.com/opensoft/openBenches)
- Source commit: [d74a1a66b08f1f3987a03172e91cc0c0298ecd1d](https://github.com/opensoft/openBenches/commit/d74a1a66b08f1f3987a03172e91cc0c0298ecd1d)
- Governed change: `openspec/changes/fix-park-handoff-integrity/`
- Sole implementation feature: `specs/177-park-handoff-safety/`
- SET-01: [PR #310](https://github.com/opensoft/openBenches/pull/310), all-leg repository/branch preflight.
- SET-02: [PR #311](https://github.com/opensoft/openBenches/pull/311), preserving unselected records.
- SET-03: [PR #312](https://github.com/opensoft/openBenches/pull/312), verifying origin before accepting an existing resumed worktree.
- SET-04: [PR #313](https://github.com/opensoft/openBenches/pull/313), retrying pending manifest publication independently of content changes and refusing exhausted push attempts.
- SET-05: [PR #315](https://github.com/opensoft/openBenches/pull/315), refreshing the receiving workspace before manifest loading with safe dirty/conflict/unavailable-origin refusals.
- SET-06: [PR #319](https://github.com/opensoft/openBenches/pull/319), descriptor-relative publication that refuses symlinked directories, unsafe selector destinations and occupied temporary paths without clobbering unrelated work.

The following copies are byte-identical to that source commit. Target paths
are relative to this assembly root; source paths are relative to openBenches.

| Target | Source | SHA-256 |
| --- | --- | --- |
| `.specify/extensions/git/scripts/bash/park.sh` | `devBenches/base-image/files/speckit-worktree/templates/specify/extensions/git/scripts/bash/park.sh` | `1ff1e60fc0a4177f69738c3354d571fe3e21d3e1e5d04f8ae7123d8d11d2eed9` |
| `.specify/extensions/git/scripts/bash/resume.sh` | `devBenches/base-image/files/speckit-worktree/templates/specify/extensions/git/scripts/bash/resume.sh` | `94116417965ae9adbd9fbb6f819752754d316de4d950f6ab8a1046dd5100ae12` |
| `.specify/extensions/git/scripts/bash/workspace-common.sh` | `devBenches/base-image/files/speckit-worktree/templates/specify/extensions/git/scripts/bash/workspace-common.sh` | `59b758a59b84d4891881dd42fb9db74f560b14347a00f76128fa97dfb3c6e410` |
| `.specify/extensions/git/scripts/bash/git-common.sh` | `devBenches/base-image/files/speckit-worktree/templates/specify/extensions/git/scripts/bash/git-common.sh` | `3fffb4a1b3bc5d1216afe90a3d811cbb7ea3162cf1115a601475653d4c0deabc` |
| `tests/runtime_tooling/test_park_handoff.py` | `devBenches/devcontainer.test/test-speckit-park-handoff.py` | `979a740681ca2c73957bfdfa52d98366b4bc21b0bb529b2b18b234346695df5c` |

All four shared helpers compared exactly against the source candidate.
The core-creation correction and core selector publication remain declared
local deviations in runtime-development.md. The core's selector publisher
body also matches the shared git-common publisher exactly. The shared resume copy
now supersedes the earlier local failed-fetch correction as well as fixing
the existing-worktree bypass. No content marker is fabricated for this
composite tooling tree, and no shape digest or product/leg pin is changed.

The source tests use only disposable local repositories and bare origins.
They run in this consumer against its own copied tooling without upstream
network reads. The test module's default path resolves this root's .specify
directory. Existing creation/resume tests remain in the same suite.
