# Stack & market research
27/11/2026 • C owns, B validates credentials and budget. Sources public; vendor feature descriptions are not independent effectiveness claims.

## Similar solutions
| Solution | Verified offering | Learning / positioning |
|---|---|---|
| Bitdefender Scamio / Scam Protection | message/link/screenshot assessment, advice | proves screenshot scan is not new; minimize context switching, Vietnamese evidence |
| Norton Genie | AI analysis of suspicious messages/screenshots | focus on actionable, non-alarmist UX and uncertainty |
| Browser URL reputation (e.g. Google Safe Browsing) | URL-centric threat signals, complementary | use only if license/terms and quota allow, not proof of fraud, not necessary for MVP |

Sources: https://www.bitdefender.com/en-us/consumer/scam-protection ; https://www.bitdefender.com/consumer/support/answer/97320/ ; https://us.norton.com/blog/online-scams/norton-genie ; https://us.norton.com/blog/online-scams/holiday-norton-report ; https://developers.google.com/safe-browsing (optional, verify noncommercial terms before use). No claim competitors lack Vietnamese or browser integration without further benchmark.

## Recommended stack
| Layer | Choice | Why / fallback |
|---|---|---|
| Extension | WXT + React + TypeScript, MV3 | scaffold fast, build unpacked; plain MV3 + TS/Vite if WXT unfamiliar |
| Web demo | Vite + React | static site served by backend same origin; plain HTML/JS if speed needed |
| Chrome APIs | activeTab, tabs.captureVisibleTab, exact host permission | user initiated screenshot; no all_urls; popup grant caveats |
| API | FastAPI + Pydantic v2 + Uvicorn | simple typed request + docs/tests; no Nest migration |
| Image | browser Canvas + Pillow | local crop/resize, server validate/reencode |
| AI primary | Gemini API via google-genai, supported Flash multimodal model with structured output | one image/text call, JSON schema; confirm available stable model using account + test; pin exact ID |
| Alternative | OpenAI vision-capable small/fast model with structured output via official SDK, only if key already available | same engine port; choose one by 27/11, avoid two integrations; verify supported model/version and costs |
| Fallback | deterministic local lexical cues | UNKNOWN only, not replacement for real AI judging |
| Testing | pytest, httpx, Vitest, browser manual + Playwright web smoke optional | no need full automation for MV3 in five days |
| Deploy | Docker + Cloud Run (or pre-approved Docker PaaS/VPS) | public HTTPS, stable URL, env/secret store, one instance for MVP limiter |
| CI/collab | GitHub Actions, GitHub Projects Kanban | lint/test/build on PR, task ID links |
| Optional after P0 | URL reputation, local QR extraction | only approved data handling/terms; never open URL |
| Not needed | Postgres, Redis, RAG, LangChain, fine-tuning, Kubernetes | scope/cost/privacy overhead |

Reference docs: https://wxt.dev/guide/essentials/config/manifest.html ; https://developer.chrome.com/docs/extensions/reference/api/tabs ; https://developer.chrome.com/docs/extensions/develop/concepts/activeTab ; https://ai.google.dev/gemini-api/docs/image-understanding ; https://ai.google.dev/gemini-api/docs/structured-output ; https://ai.google.dev/gemini-api/docs/pricing ; https://ai.google.dev/gemini-api/docs/terms ; https://docs.cloud.google.com/run/docs/deploying ; https://docs.cloud.google.com/run/docs/container-contract . Primary provider and Cloud Run docs verified conceptually; no actual key/deployment test performed. Do not assume free tier, privacy, model ID or rate limit; check live account/terms. Use synthetic content for public trial; disclose third-party processing. No user-specific data shared with providers during this planning task.

## Day 0 spike / cost control
- C tests 3 text + 3 screenshot cases, schema validity, latency, model ID, tokens, refusal and quota using synthetic data. Select one provider with successful structured output and available key. If no paid key, ask teammates immediately; do not assume free production quota.
- B tests public HTTPS from another network, billing/secret, max instances and limiter. Record per-scan usage. Estimate cost = (input token cost + output token cost + platform request/compute) × estimated scans; use real provider pricing and measured tokens (image tokens counted by provider). Define 200 planned judge/demo scans plus contingency as budgeting assumption, adjust based on team approval. Set provider quotas where available and budget alerts; reserve through 11/12. Keep public health check cheap; avoid high-frequency paid probes. Record actual rates/limits in daily log. If deployment blocked switch platform by 28/11.
