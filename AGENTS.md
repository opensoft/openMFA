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
