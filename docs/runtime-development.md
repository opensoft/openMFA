# Runtime feature development

Status: candidate tooling; assembly pins unchanged

The first challenge/receipt candidate is governed by the spec leg's
`add-challenge-receipt-core` packet and feature
`001-challenge-receipt-core`. Its paired feature checkouts live under
`worktrees/<feature>/{spec,code}/`. Canonical proposals, contracts and Speckit
files live in the spec feature; implementation and tests live in code.

This tooling was generated with the installed `setup-openspeckit` bootstrap:
Spec Kit 0.12.12.dev0 and the workBenches worktree overlay with content marker
`6eb7d974837269e8fca7a73646982f97c3277d2a7edb6b62f6349bb8ff24880b`.
The source is the workstation's canonical setup-openspeckit distribution,
not product runtime code. The marker records overlay content; it is not a
product release, package signature or dependency acceptance.

The committed subset starts from portable core scripts/templates, the git
extension/config and shell helpers. Host-local feature selectors, integration
receipt manifests, cache state and the unfilled constitution are excluded.
There is no adopted product constitution in this bootstrap. The shared
OpenSpec/Speckit protocol under `$HOME/.agents/` remains authoritative.
The current PowerShell git extension is not Triad-aware; invoke its bash
counterpart in the declared bench.

Two project-local corrections remain against that generated baseline:
core specification creation resolves the selected paired feature directory
without replacing its selector, and the core common helper publishes the
selector without following symlink destinations or truncating unrelated work.
Its publisher body matches the shared git helper. Reconcile both deviations
before regenerating core helpers, and run `tests/runtime_tooling/`.
Safe Bash publication uses Python 3 and POSIX directory descriptors in the
declared bench, as does existing worktree-state publication.

The park/handoff blockers are now repaired in the governed shared-source
candidate, openBenches PRs #310, #311, #312, #313, #315 and #319. This root copies the four corrected
helpers and focused regression suite from the exact proposed source commit
recorded in [shared park provenance](shared-park-source.md). Source landing
evidence is recorded on those PRs. The shared resume correction supersedes
the earlier local failed-fetch fix and verifies origin before accepting an
existing worktree. The declared local core deviations remain. This candidate
also retries pending manifest publication when feature content is unchanged,
refuses exhausted push attempts, and refreshes the receiving workspace under
its mutex before reading a manifest. Refresh preserves dirty work and aborts
conflicts; dry-run remains a cached preview. Manifest and selector publication
reject unsafe symlinks and occupied temporary paths without touching unrelated
targets, and preserve existing destination permission bits on replacement.
It does not claim fleet installation.

The generated overlay-content marker is deliberately omitted because this
corrected copy is no longer byte-identical to its baseline. The baseline
content hash above is provenance only; no digest is changed to hide drift.
These files are project tooling, not shape-pinned copies. All shape-pinned
files and their recorded digests remain unchanged.

From the assembly root, with both pinned legs present:

```sh
make bootstrap
bash .specify/extensions/git/scripts/bash/create-new-feature.sh --json --short-name <name> "<description>"
```

Run feature creation only once per feature. It creates paired leg branches and
prints the exact feature selection. For an existing feature use the printed
`SPECIFY_FEATURE` and `SPECIFY_FEATURE_DIRECTORY` values before follow-on
commands such as `bash .specify/scripts/bash/setup-plan.sh --json`.
Never run creation again just to select a feature.

The shape-pinned root `.gitignore` is untouched. Before creating features,
put these machine-local exclusions in `.git/info/exclude`:

```gitignore
/worktrees/
/.specify/feature.json
```

Do not stage linked worktrees or the selector; their Git plumbing can carry
machine-specific absolute paths. Local caches and generated metadata are
likewise not product source.

The root tooling PR does not advance either leg. Land reviewed spec/code PRs
first; then use the shape's normal lockstep pin mechanism. No consumer pins a
leg or a floating development branch. Local source tests and tooling validation
do not qualify real factor backends, custody, human approval or live QA.
