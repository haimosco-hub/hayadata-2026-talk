# hayaData 2026 — Accepted Session

**Status:** Accepted

**Title:** Dashboards Aren't Dying, They're Getting a Sidekick

**Description** (749 chars, as submitted):
Everyone's arguing whether AI is going to kill the dashboard or the dashboard survives. At WSC Sports we think that's the wrong fight - the future isn't dashboards vs. agents, it's dashboards with an agent embedded inside them. A stakeholder should be able to look at a report and just ask it a follow-up question, right there, without leaving the page or opening a chat window. I'll share how we're combining our agent-built HTML reports with an embedded data agent, why keeping the dashboard matters (it's still the fastest way to see a trend at a glance), what the agent adds on top (ad-hoc questions, drill-downs, explanations), and what building this hybrid actually requires - trust, grounding, and reusing the permission model we already had.

**Domain:** Data Analytics & BI (Self-Service Analytics / Semantic Layers & Metrics Management / AI-Enabled Analytics)

**Level:** Intermediate

**Format:** 15-minute talk

**Delivered before:** No — new content

**Positioning note:** This talk deliberately counters last year's hayaData Track C talk
"Silence of the Dashboards: Is AI Coming for Us All?" (David Krakov, Honeydew), which argued
conversational AI replaces dashboards. This talk argues the opposite — dashboards persist,
with an agent embedded inside them. Worth keeping that contrast sharp and intentional in the
final framing, not accidental.

**Draft talk outline (from the CFP submission, for the committee, not public):**
1. The false binary: "dashboards are dying" vs. "dashboards are all you need" — why both are wrong
2. What we already built: agent-built HTML reports + a trustworthy data agent, and why the natural next step was combining them
3. What the embedded agent adds on top of a static report: ad-hoc questions, drill-downs, explanations, without leaving the page
4. Why the dashboard doesn't go away: it's still the fastest way to see a trend at a glance — the agent handles the "why" and "what if", not the "what"
5. What this hybrid actually requires: grounding, trust, reusing the existing permission model
6. Live/recorded demo: a report, then a follow-up question answered inline
7. Takeaway: the future of stakeholder-data interaction is hybrid, not either/or

**Source material used to build this submission:**
- `reports-playground` — the agent-built HTML-report framework (Design / Copy / Snowflake
  Query Builder skills wrapped as a Claude-based agent)
- The Snowflake data agent used for ad-hoc stakeholder questions
- The existing customer permission model already used for embedding reports in the platform

---

This mirrors the same content originally drafted at `Desktop/hayaData-2026-Talk/submission.md`
(a standalone folder created 2026-09-02, now folded back into this project — see
`08_projects/speaker-development/project.md` for the working-context section covering this
talk's prep, which replaces that folder's `CLAUDE.md`).
