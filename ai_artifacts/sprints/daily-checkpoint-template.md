# Daily checkpoint template (append to existing daily-log.md, not a second tracker)

### YYYY-MM-DD HH:mm ICT — Gx
- Gate objective / verdict: accepted | partial | rejected | not verified
- Verified integration code SHA / deployment revision / public URL (if applicable):

| Lane | Merged task/PR links (or none) | Actual evidence / caveats | Next task / entry condition |
|---|---|---|---|
| A | | | |
| B | | | |
| C | | | |

- Integrated increment: what works together now; fixture-only vs real.
- Gate tests: command / pass-fail-not run / tested SHA / link.
- Blockers: exact interface, owner, next action & time; P0 vs P1.
- Decisions or deferrals: link decision-log; not duplicated.
- Next day ready work: task IDs, verified baseline SHA and dependencies.
- Context publication: current-state update PR/commit; board reconciled by B.
- Retrospective (optional, one change to working method).

Never copy previous green result onto a new SHA without qualification. Do not report a gate passed just because the day ended. Avoid raw screenshots/logs or secrets.
