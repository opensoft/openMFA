# Shared park source provenance

Snapshot: governed shared-source repair, 2026-11-10. This record binds exact
source bytes; the source PRs carry the landing evidence. Source provenance
and fleet installation remain separate acceptance gates.

- Repository: [opensoft/openBenches](https://github.com/opensoft/openBenches)
- Source commit: [46a867b62322939beae62eb1f21d27fcf6ce1720](https://github.com/opensoft/openBenches/commit/46a867b62322939beae62eb1f21d27fcf6ce1720)
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
| `.specify/extensions/git/scripts/bash/workspace-common.sh` | `devBenches/base-image/files/speckit-worktree/templates/specify/extensions/git/scripts/bash/workspace-common.sh` | `a8f8ad9048af8ca2c33ff4142df08ae0a6a5361dd17b28331782cff661719617` |
| `.specify/extensions/git/scripts/bash/git-common.sh` | `devBenches/base-image/files/speckit-worktree/templates/specify/extensions/git/scripts/bash/git-common.sh` | `bbf3bf4f18fa833ec4cfd2e5c07fdd7d5275e3e5f9dbe8b67072fae9db0bce16` |
| `tests/runtime_tooling/test_park_handoff.py` | `devBenches/devcontainer.test/test-speckit-park-handoff.py` | `279954aec08dc40b4d001dd90354e4326e7c7c5ae87744b000f430c1765b4a26` |

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
