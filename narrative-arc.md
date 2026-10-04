# hayaData 2026 — Narrative Arc (draft 4)

**Status:** in-work
**Talk:** Dashboards Aren't Dying, They're Getting a Sidekick (15 min)
**Date:** 2026-09-02; draft 3 (thesis v2, arc restructured) 2026-09-07; **draft 4 (arc re-mapped
onto the built deck, closing decided) 2026-10-04**

**Thesis (locked v2, 2026-09-07):** Every dashboard ends with a follow-up question. Leave the
page to ask an analyst and you lose time. Leave it to ask an agent and you lose context.
Dashboards don't need replacing. They need a way to answer back.
**Second line to remember:** The report is the prompt.
**Closing stance (decided 2026-10-04):** Like any other thing in the AI era, dashboards need to
adapt and upgrade. This is the next version of the dashboard, and the best way to interact
with data.

**Ground rules:** concept only, no internal WSC tooling named; mocked demo; every beat must
serve the thesis; 15 minutes is the hard wall.

---

## What changed in draft 4 (deck is now the source of structure)

Draft 3 was written before the deck existed. The deck (`presentation.html`, 19 slides) has
since made several simplifications; draft 4 adopts them instead of fighting them:

1. **One dashboard, embedded.** The "broken" flow is the Superstore Executive Overview embedded
   directly in the deck (slide 5, iframe onto `demo/dashboard.html`), clicked live. The separate
   `demo/demo-broken.html` (Furniture & Office report) is **retired** from the talk; it stays in
   the folder as reference. The "fixed" flow will become an embedded slide the same way (the
   same Executive Overview plus a text box) — **TO BUILD**; until then slide 13 hands off to
   `demo/demo-fixed.html`.
2. **The two exits are told, not shown.** Draft 3 had a Slack still and a standalone-agent mock.
   The deck has one turn slide ("someone needs to answer the follow-up question") and two
   portraits (The Analyst, The Agent). The whole cost argument is now spoken over the faces.
   Beat 2's cost table is gone from the slides; it survives below as the speaker's crib.
3. **The thesis moves to open Section 2** (it sits right after the dashboard in the deck).
4. **Beat 5 gained a frame:** "Best practices → NOT YET → just three things you can't skip."
5. **The opening keeps the 80% slide**; the SPOKEN line is still the tally ("I kept a tally for a
   month, four out of five…"), so the number on screen is a personal count, not a statistic.
   If anyone asks "source?", the answer is "my own tally".
6. **Closing decided** (Section 6): the personal stance, one title-only slide, then the thesis
   slide again, "Ask the dashboard" spoken last.
7. **Demo data honesty.** The embedded Executive Overview is built from the real Superstore
   sample (US rows), so its numbers are real. `demo-fixed.html` still runs on generated
   Furniture & Office rows; when the fixed flow is rebuilt as an embedded slide, its scripted
   answers must be computed from the same real Superstore rows as the Overview.

---

## The arc in one line
Hook (the tally, intro, one-sentence agenda) → the dashboard did its job (the Executive Overview,
live, a filter, the question is born) → the question leaves the page (thesis; the Analyst costs
time, the Agent costs context) → "why not just an agent?" (steelman, the jigsaw, the report is
the prompt) → the same page, answering back (one text box, two questions) → three things you
can't skip (grounding, trust, permissions) → the next version of the dashboard (stance, thesis,
"Ask the dashboard").

## Slide map and timing

| # | Section | Slides | Time | Job |
|---|---|---|---|---|
| 0 | The hook | 1–3 | 0:00–0:30 | Tally, intro, one-sentence agenda |
| 1 | The dashboard did its job | 4–5 (embedded Overview) | 0:30–2:00 | The glance, the filter, the question is born |
| 2 | The question leaves the page | 6–9 | 2:00–3:45 | Thesis, then the two exits through the two faces |
| 3 | Why not just an agent? | 10–12 | 3:45–6:00 | Steelman, jigsaw, "the report is the prompt" |
| 4 | The same page, answering back | 13 + demo-fixed | 6:00–8:45 | Same report, one text box, two questions |
| 5 | Three things you can't skip | 14–17 | 8:45–12:00 | Grounding, trust, permissions, one story each |
| 6 | The next version of the dashboard | 18–19 | 12:00–13:15 | Stance, thesis restated, "Ask the dashboard" |

Buffer: ~1:45. The live mock eats most of it. If the talk runs long: Section 2 shrinks first,
then Section 5's grounding and permissions stories shrink to principle + one sentence. Section
1, Section 4 and Section 6 never shrink.

---

## Section 0 — The hook (slides 1–3, 0:00–0:30)
**Job:** buy the demo the room's attention in one breath, say who you are, hand off.

**Spoken, roughly:**
> "I kept a tally for a month. Four out of five times someone opened one of my dashboards,
> they left with more questions than they came with. That's not a bug. That's a feature.
>
> I'm Haim. I lead data analytics at a sports-tech company, and I've been on both ends of
> those questions.
>
> I'll show you where those questions go today, why the obvious fix doesn't work, and what it
> looks like when the dashboard answers them itself."

- Slide 2 shows "80%"; the mouth says "four out of five, my own count". That is the whole
  defence against "source?". Do not say "eighty percent of the time" as if it were research.
- The agenda is one sentence, not a slide. The thesis is NOT stated here.

## Section 1 — The dashboard did its job (slides 4–5, 0:30–2:00)
**Job:** make the room feel the follow-up question before you name it, on a dashboard they all
recognise, with the dashboard as the hero.

- **Slide 4 (~10s).** "You've all built this dashboard. Watch what happens thirty seconds
  after someone reads it." Then advance to the embedded Overview.
- **Slide 5, the embedded Superstore Executive Overview (~75s), live.** Narrate it as a scene
  over the clicks: Monday morning, a named stakeholder opens the page. One click on the filter
  bar; a number moves the wrong way; thirty seconds in the stakeholder asks "wait — why?" Say
  the question out loud, in the stakeholder's voice. **The dashboard just succeeded: nobody
  asks that without first seeing it.**
- **Click path: TO FIX IN REHEARSAL.** The Overview's filter bar has date range, State, Segment,
  Manufacturer, Category, Sub-Category, Customer (no Region). Pick ONE filter whose result
  visibly raises a "why" (candidates: Category → Furniture and watch profit; or a single State
  with negative profit such as Texas) and make it muscle memory. One click, one question. The
  question must be the SAME one the fixed flow answers in Section 4.

**Watch:** this is the most human 90 seconds of the talk; do not let it become a product
walkthrough. No feature tour of the filter bar. A mis-click here costs the opening.

## Section 2 — The question leaves the page (slides 6–9, 2:00–3:45)
**Job:** name what just happened (thesis), then show the two places the question goes today
and what each costs. Told, not shown — the two portraits are the only visuals.

- **Slide 6, thesis (~20s).** Read it. The room has just lived lines 1–3; lines 4–5 are a
  promise Section 3 pays off. Pause after "answer back".
- **Slide 7, the turn (~10s).** "Someone needs to answer the follow-up question. Today that
  someone is one of two people."
- **Slide 8, The Analyst (~35s) — cost: TIME.** "The stakeholder opens Slack. The analyst was
  mid-something-else. Re-opens the query, re-applies the filters, finds the same number, writes
  it up. Forty minutes later the answer arrives. It works. It costs two people an afternoon and
  puts the analyst on the follow-up queue for a report they finished last week."
- **Slide 9, The Agent (~40s) — cost: CONTEXT. Spend the time here.** "Or the stakeholder opens
  a chat window and types the same question. The agent is fast, flexible — and the first thing
  it asks is: which report? which date range? which definition of profit? The human is
  re-explaining a page they were just looking at. And a wrong answer here looks exactly like a
  right one." The sharpest sentence of the talk: **"Most 'the AI gave me a wrong number' stories
  are really 'the human re-supplied the context badly.'"**

Speaker's crib (not a slide):

| Exit | Speed | Who carries the context | Cost |
|---|---|---|---|
| Slack → analyst | slow | the analyst reconstructs it | stakeholder waits, analyst interrupted — time, twice |
| Standalone chat agent | fast | the stakeholder re-explains it | workflow break + everything lost in re-explaining — context |

**Watch:** leave the room with "so the agent is the fast one, just fix its context problem" —
that is exactly the question Section 3 opens on. Do not say "embedded" yet. "Agent" here means a
STANDALONE chat agent; say so once.

## Section 3 — "Why not just work with an agent?" (slides 10–12, 3:45–6:00)
**Job:** answer the question the room is now asking with a lock-and-key picture, and land on
"put the agent on the page".

- **Slide 10, the steelman (~30s).** Put the skeptic's case up in its strongest form: "Every
  dashboard is a frozen answer to a question someone asked six months ago. The agent answers
  fresh, any question, any slice. Why keep the dashboard at all?" Let it stand. Then: "Because
  they're not competing."
- **Slide 11, the jigsaw grid (~1:30), five rows, one click each, speak to all five.** The
  winning side is big and yellow, the losing side small and grey, so the room reads "who wins
  this row" before you say it.

| Row | Dashboard | Agent | Winner |
|---|---|---|---|
| Speed of a first look | 5 metrics + 2 charts in a five-second glance | types, thinks, one answer back | dashboard |
| Flexibility & agility | only what someone predicted months ago | any cut, any slice, the moment you ask | agent |
| Shared truth | everyone argues about the same number | every answer private, phrased differently | dashboard |
| Presentation | numbers and charts; the reader interprets | words; explains the why | agent |
| Trust | certified once, read a thousand times | earned again on every answer | dashboard |

  3–2 to the dashboard, so the agent reads as a real partner, not a foil. Row 2 is why the
  follow-up leaves the page; row 4 returns as the second answer in the demo. Sixth click:
  **"They fit."** One sentence over it: "This is not a competition. This is a jigsaw."
- **Slide 12, the landing (~30s) — "the report is the prompt".** "And there is a bonus. Context
  is not a row, because neither side owns it: the dashboard PRODUCES it — the filters, the date
  range, the definitions, the number you're staring at — and the agent CONSUMES it. The
  dashboard has the context and can't use it. The agent can use context and doesn't have it.
  So put the agent on the page."

**Watch:** a comparison table could be in any AI/BI talk. The staged reveal, "They fit." and
the context bonus are what make it this talk's. No vendor names.

## Section 4 — The same page, answering back (slide 13 + fixed demo, 6:00–8:45)
**Job:** the "after" half. The SAME dashboard, the SAME filter, the SAME question — and one new
thing on the page: a text box. The question stays. Show the mechanism once, cleanly.

- **Slide 13 (~10s).** "Same dashboard. One new thing. Same filter, same question. Watch what's
  different this time." Hand off to the fixed demo (today `demo/demo-fixed.html`; later the
  embedded slide — see TO BUILD).
- **The fixed demo (~2:30), three moments, no narration over the mechanics:**
  1. **The glance.** The room recognises the page. Same filter click as Section 1. Same number
     moves. "Same page. Same question." Five seconds.
  2. **The follow-up, in place.** Type the question into the box on the page. The answer arrives
     inline and **visibly reuses the page's context** — same filter, same date range, same
     definition, no clarifying question asked. The context bonus, shown.
  3. **The drill-down + the explanation.** One follow-up to the follow-up ("which sub-category?").
     The agent slices a way the dashboard never offered (row 2) and answers in two sentences of
     words that reason across sales, discount and profit (row 4). End on the agent being useful.
- Then stop. One drill-down at most. Refusal moment stays OUT of the demo (its trust point is
  made in words in Section 5).

**Watch:** it must not look like a product. No logo, no feature tour. Scripted answers are
written the way a careful analyst would write them: cite the numbers on the page, name the
active filter, no flourish. Rehearse the click path until it is muscle memory.

## Section 5 — Three things you can't skip (slides 14–17, 8:45–12:00)
**Job:** the credibility section. The demo just made it look easy; this is what it took and what
still hurts. hayaData asked for production stories and honest tradeoffs.

- **Slide 14, the frame (~20s).** Title reads "Best practices"; one click stamps NOT YET over
  it; "Just three things you can't skip" fades in. Spoken: "I'm not going to give you best
  practices — nobody has them yet. But there are three things you cannot skip, because without
  them the context bonus from the jigsaw isn't real. The dashboard has the context; handing it
  to the agent is not free. Each of these is one piece of the handover."
- **Slide 15, Grounding (~45s) — the agent inherits, it does not infer.** The agent answers from
  the report's own query and definitions, not a fresh guess at the warehouse. *Story — the two
  profits.* The dashboard's Profit excludes returned orders. An early version queried the
  warehouse fresh and included returns. It came back with a perfectly plausible number that
  disagreed with the chart next to it by a few thousand dollars. Nobody was wrong; the
  definitions differed; the stakeholder now trusted neither. Lesson: the agent runs the report's
  query. Same definitions, same filters, same grain.
- **Slide 16, Trust (~45s) — show the work, and say "not from here".** The answer cites the
  numbers already on the page, names the active filter, says which definition it used. And when
  a question cannot be answered from the report's ground, it says so. *Story — the refusal that
  earned more than an answer.* Asked "is this because of the competition", the agent said "I
  can't answer that from this report — it has no competitor data." A stakeholder later said that
  refusal was why they believed the other answers. Lesson: "I can't answer that from this
  report" is a feature.
- **Slide 17, Permissions (~45s) — answer inside the scope, never around it.** Some filters are
  not a choice; they are the rows the viewer is allowed to see. Reuse whatever access model
  already governs the page; never build a second one. *Spoken example — one question, two
  answers.* The Central manager asks "is Central the worst region?" Unfiltered: "Central is the
  worst of the four", with three regions' numbers this viewer was never supposed to see.
  Row-level: "From this report I only see Central. It's negative for the period. I can't compare
  it to regions you don't have access to." Same question; only the second answer is allowed.
- **The hand-off (~15s).** "All three come down to one thing: someone has to decide what the
  ground is — the definitions, the scope, what this report can and cannot answer." Say it and
  STOP, without saying who. Section 6 picks it up.

**Timing:** 20 + 45×3 + 15 = 2:50. If long, Trust keeps its full story; the other two shrink to
principle + one sentence.

**Watch:** no system names, no product tour. Stories are patterns told in Superstore terms,
never tickets or dates.

## Section 6 — The next version of the dashboard (slides 18–19, 12:00–13:15)
**Job:** land it as a personal stance, not a summary. Decided 2026-10-04. No replay of the
demo, no summary of the six sections. The thesis IS the summary.

- **Slide 18 — title only: "Like any other thing in the AI era, dashboards need to adapt and
  upgrade."** (~50s spoken over it)
> "Someone has to decide what the ground is. That someone is us.
>
> I love dashboards. I'm not going to pretend otherwise on a stage. But loving something
> doesn't exempt it from the AI era. Everything in our field has to adapt — the query, the
> analyst, the dashboard. No exceptions.
>
> What I showed you today is what that adaptation looks like. Nothing about the dashboard got
> weaker. It still wins the glance, the shared truth, the trust. It just gained the one thing
> it was always missing: the ability to answer the question it raised.
>
> That's not the dashboard surviving. That's the dashboard's next version. And I believe it's
> the best way we'll have to interact with data."
- **Slide 19 — the thesis, again (~20s).** Same slide as slide 6. Read the last line only:
  "Dashboards don't need replacing. They need a way to answer back."
- **Final three words, spoken, not on the slide:** "Ask the dashboard."

Done at ~13:15. Buffer ~1:45.

**Watch:** "the best way to interact with data" is an absolute; keep it framed as "I believe",
anchored to the context argument the talk just made. Do not add a "thank you / questions"
slide; end on the thesis.

---

## TO BUILD / open items
- **Fixed flow as an embedded slide.** Same Executive Overview as slide 5 (`demo/dashboard.html`)
  plus a text box and two scripted answers, embedded via iframe like slide 5, replacing the
  slide-13 hand-off to `demo-fixed.html`. Scripted answers computed from the real Superstore
  rows the Overview already uses. Must be pixel-identical to slide 5 except for the text box.
- **The click path for Section 1 / Section 4** (one filter, one question) — fix in rehearsal,
  then write the two scripted answers to match it.
- `demo/demo-broken.html` retired from the talk (kept as reference).
- Rehearsal with a clock: Sections 1 and 4 are live; the buffer is theirs.

## Drift flags vs. the CFP outline (`accepted-submission.md`)
Unchanged from draft 3: CFP points 1+2 merged into Section 2; demo before costs; closing is a
stance plus the analyst thread ("someone has to decide what the ground is"), not in the CFP but
inside the speaker-development angle. None of these change the claims in the public abstract.

## Decided
- ~~Demo format~~ 2026-09-07: scripted mock inside the HTML deck. **2026-10-04: embedded
  Executive Overview is the ONLY "broken" dashboard; the fixed flow to be embedded the same way.**
- ~~Opening~~ 2026-09-08 tally hook; **2026-10-04: the 80% slide stays, the tally is spoken.**
- ~~Beat 5 war stories~~ 2026-09-07: the two profits, the refusal, the filter that was not a choice.
- ~~Closing~~ **2026-10-04: the personal stance — "Like any other thing in the AI era, dashboards
  need to adapt and upgrade" (title-only slide), thesis restated, "Ask the dashboard" spoken.**
