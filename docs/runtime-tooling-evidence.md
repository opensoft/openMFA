# Tooling regression evidence — 2026-11-10

## Shared park/handoff repair update

The two subsequent park blockers are fixed in shared-source PRs #310/#311
under `fix-park-handoff-integrity`, with separate constitution-compliant
task sets. Fresh Codex review at fc96c4d3e9778b471a3a04f963f6133f399597b2
found an existing-worktree resume bypass, reproduced by three origin-refusal
fixtures. Shared-source PR #312 verifies origin before that shortcut and
supersedes the earlier local resume correction. The consumer copies exact
source bytes recorded in [shared-park-source.md](shared-park-source.md).
Subsequent review at 819195462ea10a21dc535b380f538148e13252f7 found that
unchanged-content retry skipped a pending manifest commit. Shared PR #313
separates commit creation from publication and refuses exhausted push attempts.
Two fixtures reproduced unsuccessful publication being reported as success
before correction.

Review at 7ab6ea004ea3df3a7437b9dbd6395a45dfaf0ca8 found stale
receiving-workspace reads. Shared PR #315 refreshes under the mutex before
manifest loading and safely refuses dirty, conflicting or unavailable
refreshes. Four checks failed before correction; the unchanged dry-run
control passed.

## Local review and publication safety

Brett Heap authorized local review in place of the quota-blocked GitHub
reviewer. The ten-role local panel reviewed source #315 and this consumer.
It reproduced manifest temporary/directory symlink overwrites and direct
selector truncation. Shared PR #319 repairs those publication paths, while
the core helper carries the same safe publisher as an explicit local deviation.
Security re-review passed all five original-danger cases; QA also verified
preflight before either leg resets when the selector directory or temporary
path is unsafe.

The current suite has **37** cases: ten consumer-specific cases plus 27
shared handoff cases, including a real injected peer-push retry, three changed
or unverifiable-origin refusals, unchanged-origin repeat resume and pending
publication retry/refusal, and five receiving-workspace refresh cases.
It now also covers manifest temporary/directory protection, selector
symlink/hardlink publication, safe workspace-root aliases and pre-reset refusal.
All 37 current cases passed locally in 63.84 seconds. All consumer
Bash files passed syntax validation, the four shared dependencies and fixture
copy compared exactly, and `make validate` passed with both leg pins and all 11
shape digests unchanged.
Full park retains its
existing gone-feature reconciliation. The real operator workspace was not
used. Current validation results are recorded with the PR; consumer CI and a
fresh exact-head Codex request accompany this update;
source/consumer PR results and upstream landing are distinct gates.

## Earlier creation/resume correction evidence

Status: local source validation; draft PR review pending

Codex review of assembly PR #2 at 010067b8f2b3142b053dd02cccfd21ecc0e15edb
identified paired-selector loss in core creation (P1) and stale-ref use after
a failed resume fetch (P2). The isolated regression suite reproduced four
failures before the fixes, with the successful-origin control passing.

After the declared local corrections, all seven regression cases passed:
environment and selector placement (including dry run and follow-on plan),
unselected single-repo creation with and without a previous selector, and
present/deleted/unavailable origin states.
Tests create disposable repositories and bare local origins only. They never
read or write the operator's workspace manifest or production Git remotes.
The state fixtures preserve their manifest and refuse cached refs after a
failed verification.

Every bash helper passed syntax validation. `make validate` passed naming,
manifest and lockstep/shape validation after the changes. No shape-pinned
file or digest, leg pin or branch-protection rule changed. No shared source
distribution was modified.

The generated overlay marker was removed rather than claimed for modified
bytes. Its baseline hash remains provenance in runtime-development.md.
Regeneration and upstream distribution resync must reconcile these declared
local fixes; this candidate does not claim fleet-wide installation.

New CI checks and a fresh exact-head Codex request accompany the fix.
Current CI/review results belong to the PR's head; this file records local
evidence and does not manufacture merge, acceptance or release authority.
