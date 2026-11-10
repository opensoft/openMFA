Read AGENTS-shape.md first — the rules of this repository's shape.

This is the assembly root of **openMFA** (`openmfa`): the repository an
engineer clones. It holds `project.yaml`, the pins and the gate, and it mounts
the two legs.

| role | repository | path |
|---|---|---|
| assembly | `opensoft/openMFA` | `.` |
| spec | `opensoft/openMFA-spec` | `spec/` |
| code | `opensoft/openMFA-code` | `code/` |

Everything below this line is openMFA's own. The shape wrote the block above
once and does not pin this file, so how this project is built, tested, reviewed
and released belongs here and nothing upstream will overwrite it.

## Product workflow

Use the shared workflow from $HOME/.agents/AGENTS.md and the protocols under
$HOME/.agents/protocols/. Keep committed paths portable.

This is a neutral product. Governance, specifications, and design capture live
in spec/. Implementation and its tests live in code/. Feature worktrees belong
under worktrees/<feature>/{spec,code}/. Advance a leg and its root pin together
through the documented shape procedure.

Design packets under spec/ideation/brainstorm/ are non-normative. Implementing
the verifier or changing contracts requires an OpenSpec proposal and a Speckit
implementation feature. Secrets and deployment-specific tenant configuration
belong in protected custody.

Run make validate at this root after any pin or manifest change.
