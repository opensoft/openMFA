# Tooling regression evidence — 2026-11-10

## Shared park/handoff repair update

The two subsequent park blockers are fixed in shared-source PRs #310/#311
under `fix-park-handoff-integrity`, with separate constitution-compliant
task sets. The consumer copies exact source bytes recorded in
[shared-park-source.md](shared-park-source.md). All **14** current consumer
tests passed locally: seven prior tooling cases plus seven shared handoff
cases, including a real injected peer-push retry. Full park retains its
existing gone-feature reconciliation. The real operator workspace was not
used. Consumer CI and a fresh exact-head Codex request accompany this update;
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
