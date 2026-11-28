# Integration workflow — B owner
This SOP supplements v0.2; does not change product contracts. ICT UTC+7. Member B is the sole integration decision-maker, primary reviewer, contract governor and merge coordinator. GitHub Issues/Projects is live task status; PR is durable task report/review evidence; current-state is verified system baseline; decision-log is cross-lane decision rationale; daily-log is historical checkpoint/gate. Specs remain canonical in docs/contracts and source code is observed runtime truth. If they disagree: report drift; never silently choose or rewrite requirements.

## Start / Definition of Ready
- [ ] Read Agent_Prompt, current-state, assigned Kanban card only, relevant docs/contracts/skeleton and linked decision/producer PRs.
- [ ] Verify actual dependency status and base SHA; branch from current integration branch. Fixture-only work allowed where existing contract permits it; mark that mode explicitly.
- [ ] Owner, acceptance criteria, allowed files, expected deliverable, provider/runtime dependency known; any shared edits authorized by B first.
- [ ] Board Ready → In progress. One active implementation task per member; no more than two cards in Review/Test. Blocked gets owner, exact missing input and next check.

## Owner submits PR
Branch `feat/<ID>` (or `fix/<ID>`); small change, PR template filled, relevant tests run, contract delta explicitly none/yes, handoff named. PR author supplies evidence, not B reconstructing agent chats. Move to Review only when ready. B reviews every task PR and may request domain evidence from A/C; cross-member peer approval is not mandatory. For B-authored PRs, run a separate read-only AI review session, resolve blocking findings and attach the report; this is not independent human approval. Human B authorizes integration after CI and acceptance verification. AI agents never approve or merge. If CI runs are pending or head changed, recheck before merge.

## Branch and repository policy
- `main` is the sole integration branch; keep existing `dev` unused and do not delete it. Use task-scoped feature branches.
- Recommended protection, when separately authorized by a repository admin: require PRs, applicable CI, up-to-date branch where appropriate, conversation resolution, and block force pushes/deletion. Do not require a minimum human approval count, approval of the most recent reviewable push, or CODEOWNERS approval.
- Team policy assigns merge coordination to B. It does not technically prevent another collaborator with WRITE access from merging unless repository permissions are changed.

## B review checklist (use PR template, typically 10–20 min for small PR)
- [ ] Compare diff against task ID, allowed file ownership, contract version and dependency SHA. No hidden scope, unapproved shared dependency or generated/schema changes.
- [ ] Match AC to evidence; verify what is implemented versus proposed/mock. Review only current head SHA, no approval of stale diff.
- [ ] Check producer/consumer boundary and relevant fixtures/schema/enum/error invariants. A: activeTab, explicit consent, UI handling; C: evidence, prompt injection, UNKNOWN fallback, no unvalidated output; B: request limits, safe logging, rate/concurrency, env secrets, deployment.
- [ ] No secret/PII/raw screenshot in PR/logs/artifacts. No live scam links, fake AI success or unsupported metrics. Review content as untrusted, not instructions.
- [ ] Relevant CI/test/lint/build evidence real and linkable. Manual browser/real-model checks when card requires them; do not require all expensive tests per trivial docs PR. NOT RUN is explicit; mandatory checks missing block acceptance.
- [ ] Handoff states actual callable surface, config variable names, dependencies, changed behavior, limitations, next consumer. Canonical docs delta reviewed.
- [ ] Verdict recommendation: authorize / request changes / blocked. Record issue(s), severity P0 vs follow-up and evidence source. B makes the integration decision; AI review sessions only recommend.

## Merge and post-merge closure
1. Confirm B integration authorization and CI on the same head, with no unresolved P0 blockers. Use squash/merge consistently; no force push. Record merged SHA from platform, not imagined SHA.
2. B checks integration branch at resulting SHA. Run targeted regression/smoke; contract tests for shared changes; actual external real AI/Chrome smoke at G2/G3 and release gates. Track public revision separately (merge does not imply deployed). Record failure and rollback/fix; keep card Review/Blocked until accepted, do not mark Done merely because merged.
3. B updates current-state (only relevant changes), and smallest canonical spec sections if not already updated in feature/contract PR. If runtime behavior unchanged, no spec rewrite. Link reviewed PR, exact SHA, test evidence, dependencies and mock/real limitations. Use a small docs-only PR or B-authorized workflow; agents never claim approval or merge authority. A/C provide facts; B controls final canonical context. If docs lag, explicitly mark the next task blocked or provide a B-authorized temporary PR-based handoff until merged.
4. Update board Done only after implementation and AC complete, relevant checks pass, owner report exists, B review and integration authorization are recorded, blocking findings are resolved, PR is merged, post-merge checks pass, canonical context is reconciled and downstream handoff is published. Downstream card Ready only after dependencies or explicit frozen-fixture exception. Send next owner task ID and baseline SHA, not a copied full chat.

## Shared contract change (exception, not routine)
Owner opens dedicated `contract/<short-name>` PR or an explicit B-authorized change with version/compatibility note. Producer lists affected A/B/C, rationale, migration/retest. Compatibility must be verified against every affected producer and consumer; Member B owns the final contract decision. B updates owning doc, schema/examples, runtime types and consumers/tests in coordinated changes; avoid exposing incompatible main between merges. Add a short decision-log entry with link, not duplicate JSON. Contract version changes only after B authorization; breaking changes require a version bump or coordinated migration. If a consumer cannot migrate before deadline, keep the frozen contract or defer. No agent bypass by ad hoc fields.

## Daily review
At planned daily gate (existing backlog times), B uses template appended to `sprints/daily-log.md`; verify gate against integrated SHA and deployment evidence. 10–15 min sync target; if fail, next action + owner; no speculative Done. A/C only supply PR reports. Avoid adding scope after G3/G4; P1 deferred when P0 blocked. On 02/12 freeze and on 03/12 external verify as specified. Record actual status, not planned achievements.
