# Ownership map (planning skeleton only)
Do not create empty runtime stubs just to match this tree. Root below is proposed product repo; these docs go in `ai_artifacts/`.

```
repo/
  extension/                  A: WXT, React, MV3
    entrypoints/popup/        A: capture, preview, consent, results
    src/{api,components,lib}/ A: client, crop, state
    wxt.config.ts            A: manifest + backend host permissions
    tests/                   A
  demo/                       A: Vite web (same origin backend)
    src/                     A: upload/paste/sample, results
    tests/                   A
  backend/
    app/main.py              B: routing, static demo, middleware
    app/contracts.py         B: shared Python models/ports; A/C review
    app/routes/              B: healthz, analyze
    app/security/            B: validation, limiter, error envelope
    app/engine/              C: provider, prompt, policy, fallback
    tests/api/               B
    tests/engine/            C
    requirements*.txt        B: C proposes dependency via PR
    Dockerfile               B
  evaluation/                C: synthetic fixtures, labels, runner, metrics
  contracts/                 B: shared runtime schema/fixture (copy ai_artifacts/contracts once; update both in same contract PR or use ai_artifacts/contracts directly, preferred latter)
  .github/workflows/          B: CI
  compose.yaml .env.example  B
  README.md                  B: run instructions; A/C supply source declarations
  submission/                A: slides/guide, C: video, B: package/source/receipt
  ai_artifacts/              owners per README
```

No shared root dependency edits from A/C without B. A owns npm lockfiles within extension/demo. B owns backend lock; C requests additions. C cannot change response schema or API routes; A cannot change engine or API. B must not rewrite UI/engine; review via PR. B owns deployment, all sign off schema. A/C may run tests across repo without editing others. Task-specific integration PR approved by affected owners. Code owners can be configured after names assigned; avoid blanket agent edits.
