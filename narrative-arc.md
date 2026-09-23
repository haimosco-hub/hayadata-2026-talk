# hayaData 2026 — Narrative Arc (draft 3)

**Status:** in-work
**Talk:** Dashboards Aren't Dying, They're Getting a Sidekick (15 min)
**Date:** 2026-09-02; thesis revised and arc restructured (draft 3) 2026-09-07

**Thesis (locked v2, 2026-09-07):** Every dashboard ends with a follow-up question. Leave the
page to ask an analyst and you lose time. Leave it to ask an agent and you lose context.
Dashboards don't need replacing. They need a way to answer back.
(v1, 2026-09-02, superseded: "...Today it costs a stakeholder a day and an analyst an afternoon.
Answer it where it's asked." Same direction; v2 also defends the dashboard's own place.)
**Second line to remember:** The report is the prompt.

**Ground rules for this arc:** concept only, no internal WSC tooling named; generic mocked
demo; every beat must serve the thesis; 15 minutes is the hard wall.

---

## The arc in one line
Opening (the tally: four in five leave with more questions, not a bug, a feature; one-line intro; one-sentence agenda; hand-off) → the broken flow, shown (the dashboard
did its job; the question leaves the page and breaks twice) → the two exits and what each costs
(analyst = time, agent = context) → "why not just work with an agent?" answered by the jigsaw
(each one's weakness is the other's strength; bonus: the dashboard already holds the context
→ put the agent on the page) → the same flow, fixed (same dashboard, one text box, the question
stays) → the must-haves (grounding, trust, permissions as the handover of context) → Beat 6
(PARKED — wrap-up to be decided).

**Structure notes (draft 3, 2026-09-07):**
- Beats 1 and 4 are a BEFORE / AFTER on the SAME mocked Superstore dashboard; the only visible
  difference is the embedded text box.
- The order follows how a skeptic thinks: I saw it break → I know what each exit costs → so why
  not go all-in on the agent? → here is why not → here is the fix. The jigsaw answers a question
  the room is already asking.
- The thesis still lands at the end of Beat 1. Sentences 1-3 the room has just lived; sentences
  4-5 ("dashboards don't need replacing, they need a way to answer back") are a PROMISE that
  Beat 3 pays off.
- "Embedded" has no beat of its own: it arrives at the end of Beat 3 (jigsaw → context bonus →
  "so put the agent on the page") and Beat 4 opens on it.

---

## Opening — the tally (0:00–0:30)
**Job:** buy the demo the room's attention in one breath, say who you are, and hand off. Beat 1
is the real hook; this is the runway. (Decided 2026-09-08. Costs ~10s more than the original
20s budget — paid from the buffer.)

**Spoken, roughly:**
> "I kept a tally for a month. Four out of five times someone opened one of my dashboards,
> they left with more questions than they came with. That's not a bug. That's a feature.
>
> I'm Haim. I lead data analytics at a sports-tech company, and I've been on both ends of
> those questions.
>
> I'll show you where they go today, why the obvious fix doesn't work, and what it looks
> like when the dashboard answers them itself. You've all built this dashboard. Watch what
> happens thirty seconds after someone reads it."

**Why "I kept a tally" and not "80% of the time":** an invented statistic in the first ten
seconds is the one thing that can cost the whole talk with this committee if a single person
asks "source?". A personal count is concrete, credible, and keeps the number. Alternatives
considered: a definition-shaped version with no number ("more questions out than in isn't a
bug, it's the job"); asking the room for the number.

**The agenda is one sentence, not a slide.** "Where they go today / why the obvious fix
doesn't work / what it looks like when the dashboard answers them itself" is the three turns
of the talk without spoiling any of them.

**Watch:** the thesis is NOT stated here — it still lands at ~2:15 after the room has lived
it. The hand-off line is the last thing said before switching to demo-broken.html.

## Beat 1 — The broken flow, shown (0:30–2:15)
**Job:** make the room feel the follow-up question before you name it — by SHOWING the flow
break on the dashboard they all know, with the dashboard as the hero. (Rebuilt 2026-09-07: draft
1 told this as a story; it is now the "before" half of a before/after mock. Same Superstore
dashboard as Beat 4, minus the text box.)

Narrate it as a scene OVER the clicks — the mock is the footage, you are the voice-over. Monday
morning, a named stakeholder, a named analyst mid-something-else. Do not let it feel like a
product walkthrough.

Three cuts:
- **The dashboard (~30s).** The Superstore report on screen — "you have all built this one."
  Filter Region to Central. Profit goes negative. Thirty seconds in the stakeholder asks: "wait
  — why is profit negative in Central?" The dashboard just *succeeded*: nobody asks that
  without first seeing the dip.
- **Exit one — the analyst (~30s, a STILL, not a live mock).** A mock Slack message with the
  question. A clock jumps forward 40 minutes. The analyst was mid-something else, re-opened the
  query, re-applied the filters. The reply arrives. Cost: **time**, for both of them.
- **Exit two — the agent (~45s, the real mock — this cut carries the argument only this talk
  makes).** A standalone chat window. The stakeholder types the same question. The agent
  answers with questions: "Which report? Which date range? Do you mean profit before or after
  returns?" The stakeholder is re-explaining a page they were just looking at — and a wrong
  answer here would look exactly like a right one. Cost: **context**.

Land the thesis at ~2:15, on its own slide. The room has lived sentences 1-3; sentences 4-5 are
the promise Beat 3 pays off.

**Watch:** this is still the most human two minutes of the talk; the mock must not make it
mechanical. Beats 1 and 4 must be PIXEL-IDENTICAL except for the text box — if anything else
differs, the room credits the redesign, not the agent. Two live mocks in fifteen minutes means
both click paths are muscle memory; a mis-click here costs the opening. If it runs long, the
Slack still shrinks, never the agent cut.

## Beat 2 — The two exits, and what each costs (2:15–3:45)
**Job:** the room just watched both exits fail; now name the cost of each, and who pays. Short,
explanatory, no argument yet. (Draft 3, 2026-09-07 — carved out of the old three-homes beat;
"embedded" is NOT introduced here.)

| Exit | Speed | Who carries the context | Cost |
|---|---|---|---|
| Slack → analyst | slow | the analyst reconstructs it | stakeholder waits, analyst interrupted — **time**, twice |
| Standalone chat agent | fast | **the stakeholder re-explains it** | workflow break + everything lost in re-explaining — **context** |

- **The analyst (~35s).** "Works. Costs two people an afternoon and puts the analyst on the
  follow-up queue for a report they finished last week." The two-sided pain: the stakeholder
  waits, the analyst is pulled out of the thing they were doing.
- **The agent (~50s) — spend the time here.** "Fast, flexible — and the first thing it asks is
  which report, which filters, what do you mean by profit. The human carries the context across,
  and carries it badly." Which report? Which date range? Which DEFINITION — the report's, or the
  one the agent guesses? The sharpest sentence in the talk goes here: **"Most 'the AI gave me a
  wrong number' stories are really 'the human re-supplied the context badly.'"**

**Watch:** Beat 1 SHOWED the exits fail; Beat 2 EXPLAINS why and who pays. If it feels like a
repeat in rehearsal, Beat 2 shrinks, never Beat 1. Do not mention embedding yet — the room
should be left with "so the agent is the fast one, just fix its context problem," which is
exactly the question Beat 3 opens on.

## Beat 3 — "Why not just work with an agent?" → the jigsaw (3:45–6:15)
**Job:** answer the question the room is now asking out loud — "the agent is the fast one, so
why not work directly, entirely, with an agent?" — with a lock-and-key picture: every weakness
of one is the strength of the other. Ends by landing on "put the agent on the page." (Draft 3,
2026-09-07. "Agent" in this beat = a STANDALONE chat agent — say so once at the top, or the room
hears you arguing against your own solution.)

**The opener (~30s) — steelman it first.** Put the skeptic's case up in its strongest form: "Every
dashboard is a frozen answer to a question someone asked six months ago. The agent answers
fresh, any question, any slice. Why keep the dashboard at all?" Let it stand for a beat. Then:
"Because the two are not competitors. Look." → the table.

**The jigsaw (~1:45) — the table, five rows, speak to all five:**

| Dimension | Dashboard | Standalone agent |
|---|---|---|
| Speed of a first look | Fast. 5 metrics + 2 charts in a five-second glance | Slow. User types, agent thinks, one answer comes back |
| Flexibility & Agility | Only what someone predicted — the drill paths were decided months ago | Any cut, any slice, any new question, the moment you ask |
| Shared truth | Everyone sees the same page, argues about the same number | Every answer is private, phrased differently, possibly a different number |
| Presentation | Numbers and charts. The reader does the interpreting — and everyone interprets differently ("a chart is a number that refuses to explain itself") | Words. Summarizes, explains the why, tells the story behind the number |
| Trust | Certified once, read a thousand times | Earned again on every single answer |

Dashboard wins rows 1, 3, 5; the agent wins rows 2 and 4 — 3 to 2, so the agent column reads
as a real partner, not a foil. Row 2 is exactly why the follow-up leaves the page (Beat 1);
row 4 (presentation, added 2026-09-07) is already promised in the abstract and reappears as the
third thing the embedded agent adds in the demo, and as "show the work" in Beat 5.

**The reveal (the visual does the arguing):** show the dashboard column alone, strengths green,
weaknesses grey. Then the agent column alone, same colours. Slide them together: every grey cell
sits next to a green one. One sentence over it: "This is not a competition. This is a jigsaw."

**The bonus — context (~5:45):** context is NOT a row, because neither side owns it: the
dashboard PRODUCES it, the agent CONSUMES it. After the columns interlock, one more line appears
under the table: "And there is a bonus. The dashboard already built the context — the filters,
the date range, the definitions, the number you are staring at. Give that to the agent and the
follow-up stops being a question from scratch." Land the second line here, ~6:00:
**the report is the prompt.** (Moved up from Beat 3 at 6:30 in draft 1 — the demo at 7:00
exists to show it, so it should be in the room before the demo.)

Rows considered and dropped 2026-09-07 (pull one back if the beat feels thin): finding the
question (shows what you did not know to ask vs. answers only what you asked — the strongest of
the three, pairs with row 1); works without a person; cost of change.

**The landing (~15s) — "embedded" arrives here, not in a beat of its own.** "The dashboard has
the context and cannot use it. The agent can use context and does not have it. So put the agent
on the page." Beat 4 opens on exactly that.

Optional garnish, not structure: the see/wonder/ask loop; one wordless analogy slide (map +
turn-by-turn voice, or the car dashboard + warning light). Use at most one; the beat is 2:30.

**Watch:** a comparison table is a slide that could exist in any AI/BI talk. The interlocking
reveal and the context bonus are what make it this talk's. No vendor names, no logos.

## Beat 4 — The same flow, fixed (6:15–9:30)
**Job:** the "after" half. The SAME Superstore dashboard from Beat 1, the SAME filter, the SAME
question — and one new thing on the page: a text box. The question stays. Show the mechanism
once, cleanly, on the same page as the slides. The demo has a
script written for it by the jigsaw: it must show the two rows the agent won (flexibility,
presentation) plus the context bonus. (Rebuilt 2026-09-07.)

**Format (decided 2026-09-07):** the whole deck is an **HTML presentation**, and the demo is a
**scripted mock built INTO the deck** — not a recording, not a live call to a real system.
A mocked report with a working filter control; the filtering action is what surfaces the drop
and raises the follow-up question; the question goes into an embedded text box on the report
and a pre-scripted answer comes back inline. Deterministic like a recording, feels live to the
room, nothing leaves the page — which is the thesis, physically. Mock mechanics and the toy
dataset are LATER work (see open items).

**Four moments, ~40s each, no narration over the mechanics:**
1. **The glance.** The Beat 1 report again — the room recognises it — with one addition, the
   text box. Filter Region to Central. Profit goes negative. "Same page. Same question." Five seconds. The dashboard doing its job — row 1.
2. **The follow-up, in place.** Type "why is profit negative in Central?" into the box on
   the page. The answer arrives inline and **visibly reuses the page's context** — same
   region, same date range, same profit definition, no clarifying question asked. The context
   bonus: the report is the prompt.
3. **The drill-down.** One follow-up to the follow-up: "and which product line?" The agent
   slices a way the dashboard never offered. Row 2, flexibility & agility.
4. **The explanation.** The answer is two sentences of words, not a chart: "Tables in Central sold
   well but at 30-40% discounts, and every discounted order lost money; the other regions are
   thin but positive." Row 4, presentation. End here, on the agent being useful.

Then stop. One drill-down at most.

**Refusal moment ("I can't answer that from this report"): OUT** (decided 2026-09-07). Its
trust point is made in words in Beat 5 instead.

**Toy dataset (decided 2026-09-07, replacing the campaign-data idea from earlier the same day):
the Tableau Superstore sample.** The fictional US office-supplies retailer that ships with
Tableau Desktop: ~10k order lines over four years; Order Date, Ship Mode, Customer, Segment
(Consumer / Corporate / Home Office), Region (Central / East / South / West), State, City,
Category (Furniture / Office Supplies / Technology), 17 Sub-Categories, measures Sales,
Quantity, Discount, Profit; small Returns and People tables alongside.

Why Superstore beats an invented dataset: it is the most famous dashboard dataset in the world
and half the room has built a Superstore dashboard themselves — using it is a wink ("you have
all seen this dashboard; now watch it answer back"), nobody has to learn the domain, and it
carries a real, well-known story nobody has to invent: Furniture has thin margins, the Tables
sub-category loses money, and the Central region (Texas, Illinois) is dragged negative by heavy
discounting. Because the data is public and real, the scripted answers can be ACTUAL computed
numbers — nobody in the room can catch a made-up figure. Do this when building the mock.

- Metrics for the glance: Sales, Profit, Quantity, Orders, Profit Ratio. Two charts: monthly
  Sales + Profit over time; Profit by Region.
- Segment for the filter: Region (→ Central). Alternative: Category (→ Furniture).
- Time axis: monthly (four years of data, so not weekly).
- Slice for the drill-down: Sub-Category (→ Tables); alternative: State (→ Texas).
- The cause: discounting. Sales held, profit fell → pricing, not demand.

Demo script with the dataset in place:
1. Filter Region to Central. Profit goes negative in a stretch of months.
2. "Why is profit negative in Central?" → answer reuses the page: Central, the visible date
   range, profit as defined on this report — no clarifying question.
3. "Which sub-category?" → Tables carries the loss, Binders and Bookcases behind it.
4. "Tables in Central sold well, but the average discount ran around 30-40%, well above the
   other regions, and every discounted Tables order lost money. Sales up, profit down — which
   points at pricing, not demand. Furniture in the other three regions is thin but positive."
   (Reasons across Sales, Discount and Profit in words: the presentation row, shown not told.)
   Verify every figure against the actual data before it goes in the mock.

Still open for the mock build: the exact computed numbers, the filter control, the text box,
scripted answers.

**Watch:** it must not look like a product. No logo, no branded UI, no feature tour. Answers
are pre-scripted, so write them the way a careful analyst would — cite the numbers on the page,
name the filter that is active, no flourish. If it looks like a screenshot from a vendor deck,
it has failed. Rehearse the click path until it is muscle memory; a mis-click in a mock is
worse than a wifi story because it looks like the product broke.

## Beat 5 — The must-haves (9:30–12:30)
**Job:** the credibility section. The demo just made it look easy; this is where you say what it
took and what still hurts. hayaData asked for production stories and honest tradeoffs — this
beat delivers them. (Written 2026-09-07. War stories chosen by Haim from a Superstore-framed
list; each is a real class of failure, told in Superstore terms so no internal system is named.
"We" and "the report" are the nouns; stories are patterns, never tickets or dates.)

**The frame (~15s).** Do not present grounding, trust, permissions as three virtues. They are
the three things you must build for the context bonus from Beat 3 to be real. The dashboard has
the context; handing it to the agent is not free. Each requirement is one piece of the handover.

**Must-have 1 — Grounding: the agent inherits, it does not infer (~45s).**
The agent answers from the report's own query and definitions, not from a fresh guess at the
warehouse. Two people asking the same question must get the number the page shows.
*War story — the two profits.* The dashboard's Profit excludes returned orders. Asked "why is
profit negative in Central," an early version queried the warehouse fresh and included returns.
It came back with a perfectly plausible number that disagreed with the chart sitting next to it
by a few thousand dollars. Nobody was wrong — the definitions differed — and the stakeholder now
trusted neither. Lesson: the agent runs the report's query. Same definitions, same filters,
same grain. Inherited, not inferred.

**Must-have 2 — Trust: show the work, and say "not from here" (~45s).**
The answer cites the numbers already on the page, names the filter that is active, and says
which definition it used. And when a question cannot be answered from the report's ground, it
says so instead of improvising.
*War story — the refusal that earned more than an answer.* Asked "is this because of the
competition," the agent said: "I can't answer that from this report — it has no competitor
data." A stakeholder later said that refusal was the reason they believed the other answers.
Lesson: "I can't answer that from this report" is a feature, not a failure. (This is where the
refusal moment cut from the demo now lives — in words.)

**Must-have 3 — Permissions: answer inside the scope, never around it (~45s).**
The report was already scoped to this viewer. The agent stays inside that scope. The move that
saves months: reuse whatever access model already governs the page; do not build a second one.
*Slide (2026-09-15): lean, like the other two — title "Permissions" + "Some filters
aren't a choice — they're the rows the viewer is allowed to see. The agent answers for the page
the viewer has, not the table the warehouse has." The example below is spoken, not shown.*
*Spoken example — one question, two answers.* The Central manager asks "Is Central the worst
region?" Unfiltered, the agent says: "Central is the worst of the four — West, East and South
are all positive, Central is negative," with three regions' numbers this viewer was never
supposed to see. Row-level, it says: "From this report I only see Central. It's negative for the
period, driven by Q3. I can't compare it to regions you don't have access to." Same question;
the second answer is the only one this viewer should ever get.
*War story — the filter that was not a choice.* The dashboard was filtered to Central. For the
Central manager that filter is not a click — it is what they are allowed to see. The first
version ran its query unfiltered and answered "Central is the worst of the four regions," with
the other three regions' numbers, which that manager was never supposed to have. Lesson: every
filter on the page is part of the question, and some of them are permissions. The agent answers
for the page the viewer has, not the table the warehouse has.

**The hand-off (~15s).** The last must-have points at one person: someone
has to decide what the ground is — the definitions, the scope, what this report can and cannot
answer. End on "someone has to decide what the ground is" and STOP, without saying who. Beat 6
picks it up.

**Timing:** 15 + 45×3 + 15 = 2:45 on paper (the honest-bill list was cut 2026-09-15). If it runs long,
Trust keeps its full story and the other two shrink to principle + one sentence of story.

**Watch:** no system names, no product tour. The war stories are told in Superstore terms and
as patterns ("the first time we let it guess," never a ticket). If a story starts sounding like
a feature, cut to the lesson.

## Beat 6 — PARKED (12:30–~14:00)
**Status (2026-09-07): set aside until the wrap-up is decided, together with the Opening.**
Draft-2 version kept below for reference — payoff-only, no replay (Beat 4 already showed the
fixed flow). Candidates on the table: what changed for the two people from Beat 1; the analyst
shift (follow-up queue → defining the ground the agent stands on); thesis restated; final three
words "Ask the dashboard." Budget: whatever Opening + Beat 6 share of the remaining ~1:30 plus
buffer.

<details><summary>Draft-2 Beat 6 (reference)</summary>

**Job:** land it. No replay — Beat 4 already showed the fixed flow on the same page. This beat is
pure payoff. (Rebuilt 2026-09-07.)

- **What changed for the two people in Beat 1 (~20s).** One line each: the stakeholder never
  opened Slack, never opened a chat window. The analyst was never interrupted.
- **What changes for the analyst (~40s) — the quiet payoff for the analysts in the room.** The
  analyst's job shifts from being the **follow-up queue** to **defining the ground the agent
  stands on**: the definitions, the scope, what this report can and cannot answer. Less
  answering, more deciding what a good answer is. (Picks up the thread Beat 5 ends on —
  "someone has to decide what the ground is.")
- **Thesis, restated (~20s).** On its own slide, the same slide as at 2:00.
- **Final three words:** "Ask the dashboard."

Done at ~13:45; 75 seconds of buffer.

**Watch:** resist adding a summary slide of the six beats. The thesis IS the summary.


</details>

---

## Drift flags vs. the CFP outline (`accepted-submission.md`)
Deliberate reshaping, not silent rewriting — the CFP outline was a draft:
1. **CFP points 1+2 merged and shortened** into Beat 2. "What we already built" collapses to
   one generic line, per the strip-internal-WSC-system decision.
2. **Demo moved BEFORE costs** (CFP had costs at 5, demo at 6). Reason: the cost section
   lands harder once the room has seen the mechanism — and it lets the talk end on honesty
   and the analyst payoff rather than on a demo. Reversible if rehearsal says the demo is
   the climax.
3. **New closing payoff (analyst role shift)** — not in the CFP outline, but squarely inside
   the speaker-development angle (AI's impact on the analyst's work). Adds ~45 seconds; paid
   for by shortening the false-binary section.
None of these change the claims made in the public abstract.

## Open questions for Haim
- ~~Demo: recorded or live?~~ DECIDED 2026-09-07: scripted mock inside the HTML deck. Dataset DECIDED 2026-09-07: the Tableau Superstore sample (Region → Central, profit negative, Tables + discounting). Still open: the mock mechanics (numbers, filter control, text box, scripted answers).
- ~~Opening~~ DECIDED 2026-09-08: the tally hook + one-line intro + one-sentence agenda + hand-off (0:00–0:30).
- Beat 6 / wrap-up: still PARKED. The analyst-shift payoff is the leading candidate.
- ~~Beat 5 war stories~~ CHOSEN 2026-09-07: the two profits (grounding), the refusal that earned trust (trust), the filter that was not a choice (permissions) — all told in Superstore terms.
