# Reference audit: LIBIF → ScamLens VN
Source: selected Library `/Google Drive/ai_artifacts`, not the new repo. Read selected files from exact folder, including user-specified `prompts/Agent_Prompt.md` (Drive ID 1igtfimcdoOoaokILAHq76QE5Tya9lo8C). The project is a four-person enterprise library app (Next/Nest, DB, worker), so reuse method, not implementation/stack.

| Source examined | Observation | Adaptation |
|---|---|---|
| prompts/Agent_Prompt.md (all 283 lines) | canonical read order, strict member lanes, no cross-lane edits, documentation source of truth, quality gates | short agent guide with task prompt, PR report |
| docs/team_backlog_80_90_completion.md (first 100 lines in detail; remaining section structure and selected rules) | four lanes, explicit task IDs, scope/validation, shared conflicts and integrator | 3 lanes, Kanban tasks AC + dependencies + single board |
| docs/phase-7-wave-1-2-foundation-contract-freeze.md | shared contracts before parallel feature work; narrow producer/consumer port; tests | freeze API/AI port + fixture 27/11; one shared owner |
| docs/api-contracts.md | endpoint table, DTO, stable error envelope, deferred vs live | one analyze endpoint + health, schema & sample, error semantics |
| docs/architecture-alignment.md | modular single app, ownership, stack/gates | one container, engine port, no DB/queue |
| docs/screen-matrix.md, component-inventory.md, ui-decisions.md, workflow-state-machines.md | route/state/component responsibilities and canonical visual semantics | combine into one short UI/workflow doc with finite states |
| skeletons/README.md | planning maps, not runtime placeholders | one tree + lane ownership |
| sprints/README.md, sprint 23/07 and 24/07 (first 100 lines each) | one-day cadence, reviews based on actual PR/test evidence, partial acceptance explicit | one daily-log template per day, no fabricated sprint evidence |
| docs/phase-7-wave-4-p0-integration.md, phase-7-wave-6-7-closure.md; plans/plan-phase-7-admin-operations-users-reporting-settings-2026-07-23.md (sampled) | P0 stop conditions, cross-lane verification, truthful security claims, scope deferral | live vertical slice gate, end-to-end regression, no unverified protection claims |
| docs/phase-8-handoff.md | frozen baseline, risks, explicit deferrals, entry gates | release checklist/hold gate and handoff |

Root listing showed docs, plans, prompts, research, skeletons, sprints, stitch_design. Recursive Library listing unsupported; inspected first-level listings; did not read every individual plan, sprint, design export, or nested skeleton, and several long docs were sampled rather than exhaustively read. No LIBIF code/assets copied; original folder untouched. New files are recommendations; group must approve scope/model/platform. Daily sprint records in reference were historical Scrum; here daily checkpoints are Kanban flow reviews, not Scrum sprints. No duplicated separate progress/backlog truth.
