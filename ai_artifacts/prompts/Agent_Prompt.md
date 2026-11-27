# Agent guide — ScamLens VN
Canonical onboarding and execution contract; inspired by LIBIF Agent_Prompt, simplified. Read this before changing code.

## Read order
1. `ai_artifacts/README.md`, `docs/product-brief.md`, `plans/kanban.md` (current card/AC; check live board).
2. `skeletons/README.md` for file ownership and `docs/architecture-alignment.md`.
3. `docs/api-contracts.md` and `contracts/` for all cross-lane work; `docs/ai-contract.md` for C; `docs/ui-workflow.md` for A; `docs/release-checklist.md` for B; daily-log latest entry.

## Non-negotiable
- Product AI core is real multimodal scam-risk assessment, not simulated success. Don't implement unrelated breadth or train model. Never claim verified safe/fraud, prevention guarantee, or unmeasured performance. Treat uploaded content as untrusted. Never send raw secrets/PII to code tools, log input or save screenshot history. Do not put real provider key in code, examples, client, Git or output.
- Work only assigned task ID, allowed directories and acceptance criteria. Read repo before modifying; do not recreate working foundations. Don't edit other members' code, root shared files or schema unless explicitly assigned. Cross-lane dependency: report exact contract and owner, stop that part, use approved fixture locally; no hidden incompatible workaround.
- Source of truth: API doc + JSON schemas, AI rubric doc, UI workflow doc, live Kanban board, skeleton ownership. If mismatch, report, do not silently pick one. Change smallest relevant doc in same PR; do not append conflicting history. Breaking interface changes need A/B/C review and corresponding fixture/schema/consumer update. B owns integration branch/main and deployment. Small PR per card; no force push; do not auto-merge or claim tests run if not executed.
- Keep changes minimal; no unnecessary services; no live scam URLs. Tests use synthetic fixtures and mocks labeled as mock; release needs real AI call. When task ends, stop and report.

## Copy/paste task assignment
```text
You are Member [A|B|C], implementing [TASK-ID] for ScamLens VN.
Read ai_artifacts/prompts/Agent_Prompt.md and follow its read order.
Goal and acceptance: [copy from plans/kanban.md or board].
Allowed edits: [owned paths from skeletons/README.md + task].
Forbidden edits: all other lanes, shared schemas, dependencies, CI/root config unless explicitly assigned.
Inputs: [frozen contract version, dependency PR/commit, fixture].
First inspect existing code, identify blockers and propose concise plan. Implement only this card. For dependency conflicts report the exact file/interface and owner rather than patching another lane. Use synthetic data; never expose secrets.
Run relevant tests/lint/build and report exact command and real result. No fabricated results. Update only owned docs and handoff. Stop at acceptance or blocker.
Return: task ID, changed files, tests (pass/fail/not run), actual evidence, dependency/limitations, next handoff, suggested PR title.
```

## PR template
```
Task: Axx/Bxx/Cxx
Scope / non-scope:
Contract version + dependency commits:
Changes:
Verification commands and actual output:
Privacy/security checks:
UI evidence (if applicable):
Known limitations / blocked items:
Reviewer and handoff:
```
