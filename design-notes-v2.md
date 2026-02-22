# WRGO Design Notes — v2.0
## What Changed and Why

**Date:** 2026-02-22
**Scope:** Full rules revision targeting 3–10 player scalability and 2024–2025 party game market alignment.

---

## Market Context

The 2024–2025 party game market rewards:
1. **Simultaneous or near-simultaneous engagement** — So Clover!, Just One, Wavelength. Nobody waits passively.
2. **Short feedback loops** — Quiplash delivers a punchline and a score within 90 seconds per prompt. Players never feel stranded.
3. **Light cognitive load with high social output** — Herd Mentality, That's Not a Hat. Rules explained in 2 minutes, chaos ensues.
4. **Emergent narrative / shared memory** — the best moments from these games are stories you tell afterward.

WRGO's identity — conspiracy humor, performative presenting, hostile Q&A — is excellent and differentiated. The problem was entirely structural: downtime, player count ceiling, and scoring math that didn't scale.

---

## Change 1: Player Count — 2–6 → 3–10

**Problem:** The box said 2–6. The actual sweet spot for this game's mechanics is 5–8. At 2, there's no panel. At 3, barely one. And the market wants 3–10 on the box.

**Solution:** Hard floor at 3 (minimum viable panel of 2). Hard ceiling at 10 (panel management becomes unwieldy above that). The game's social dynamics actually improve at 6–8 — more voices in Interrogation, more dramatic voting reveals.

**Why this required other changes:** At 10 players, each turn is 8 minutes with the old structure. That's 80+ minutes per round-robin, before anyone hits the win condition. Unacceptable. So turn timing had to compress.

---

## Change 2: Conviction Target — Fixed 20 pts → Scaled by Player Count

**Old problem:** 20 points with 3pts/BELIEVER and 9 Panel members meant a Theorist could earn 27 points in a single turn (9 BELIEVERs × 3 + unanimous bonus). Simultaneously, at a 4-player table the max per turn was 9 pts (3 BELIEVERs), making 20 points a ~3-turn grind minimum. The fixed target was broken at both ends.

**Solution:** Scaled targets — 15/12/10/8 by player bracket. At 9–10 players, 8 pts is achievable in one strong turn (4 BELIEVERs × 2pts = 8), which is the right amount of tension. At 3–4 players, 15 pts requires roughly 3–4 solid rounds, which is the right game length.

**BELIEVER value reduced from 3 pts to 2 pts:** At large tables, 3pts × 9 votes = a possible 27 pts/turn. This trivialized the win condition and made single-turn swingy. 2pts is still meaningfully better than SKEPTIC (1pt) but doesn't break large-table math.

---

## Change 3: Planning Phase — 2 Minutes → 60 Seconds

**Problem:** 2 full minutes of silence at a party is a vibe killer. The Theorist is scribbling; the other 9 people have nothing to do except stare at the ceiling.

**Solution:** 60 seconds. This is enough time to write a basic argument structure. Anything beyond that is overthinking a comedy improv game.

**Companion change:** Panel now uses the PLAN phase to write their question. This is the most important structural improvement in v2. It means:
- Zero players are passive during PLAN.
- Interrogation has guaranteed substance — everyone has a prepared attack.
- Panel members don't blank out under pressure during Q&A.
- The Theorist faces a guaranteed full panel of questioners, not just whoever speaks up.

This mechanic is directly borrowed from the structural insight behind So Clover! and Just One — simultaneous action during setup phases eliminates downtime.

---

## Change 4: Interrogation — 2 Minutes → 90 Seconds

**Problem:** 2 minutes of Q&A is actually fine at 4 players. At 10 players it turns into a mob. The written question system (Change 3) guarantees coverage in less time.

**Solution:** 90 seconds. With 9 Panel members each holding a written question, 90 seconds is genuinely intense. No one's waiting for someone to think of something to ask. The pace is higher and the Theorist is under more pressure, not less.

---

## Change 5: CITATION NEEDED — Majority Vote → Individual Caller Decides

**Old rule:** Panel member calls CITATION NEEDED → Theorist answers → majority show of hands decides if it was good → +1 pt. Max 2 per Q&A.

**Problems with the old rule:**
- Stopping Q&A for a show of hands is a 30-second interruption.
- "Max 2 per Q&A" requires tracking.
- Who decides what counts as a good fake citation? Majority vote on a comedy answer is weird.

**Solution:** The Panel member who called it decides alone. This creates a personal dynamic between questioner and Theorist, rewards sharp answering, and removes the procedural stop. Max-per-Q&A cap removed — anyone can call it once (per the existing "once per Q&A" per player), which is a natural limit since there's only 90 seconds.

---

## Change 6: Discards Face-Up (Made Default, Not Optional)

**Old rule:** Discards were face-down by default; face-up was an optional "Public Discard" rule.

**Problem:** Face-up discards are strictly better for the game. They give Panel ammunition ("We noticed you rejected the CIA option..."), they fuel Cinematic Universe Mode, and they create table-wide awareness of what cards exist. There is no argument for hiding discards by default in a social deduction/performance game.

**Solution:** Face-up discards are now the default, universal rule. Public Discard is removed from optional rules (it no longer needs to exist as an option).

---

## Change 7: Large Table Mechanics (7–10 Players)

**New mechanics added:**

**Chief Skeptic (8+ players):** One Panel member elected before Interrogation who gets the last question and one mid-answer interruption. This channels the chaos of 8+ people competing to ask questions into a structured finale. The Chief Skeptic role rotates; everyone gets it eventually.

**Floor Rule (9–10 players):** Theorist may veto one question entirely per Q&A ("That line of questioning has been classified"). This prevents dogpiling — at 10 players, every angle gets attacked simultaneously, which stops being fun and starts being unfair. One veto per turn is a pressure valve.

Both mechanics add flavor consistent with the game's tone (congressional hearings, classified information) while solving real logistical problems.

---

## Change 8: THE LEAK — Mechanic Clarified and Rewarded

**Old rule:** THE LEAK was described but the reward structure was vague. The Theorist wrote a note and passed it; the receiving player read it aloud. That was it.

**Solution:** Added +2 bonus points if THE LEAK demonstrably changed at least one vote (honor system). This makes THE LEAK a meaningful strategic play, not just chaos for chaos's sake. The Theorist now has a reason to write a compelling note — it's worth 2 pts on top of whatever the round yields.

---

## Change 9: Timer Clarification — Two Timers Replaced

**Old box:** Two sand timers (90 seconds, 2 minutes).

**New box:** Two sand timers (60 seconds, 90 seconds). Both phases now use 90-second and 60-second timers rather than 2-minute timers. Removes a timer from the component list (the 2-minute timer is now unused) and matches the revised phase timings.

---

## Things Deliberately Kept

**The three-phase theory structure (ACTOR + ACT + EVIDENCE):** Perfect. Do not touch it. It forces an instantly comprehensible conspiracy theory every time.

**Conspiracy Boost Cards:** Strong mechanic, no changes to card content. These are the best source of escalating absurdity in the game.

**ALLY REVEALED and THEY'RE IN THIS ROOM:** Technically tricky but genuinely funny when executed. Kept.

**Best Question Award:** This is excellent design — it gives the Theorist meaningful post-round interaction, requires the Theorist to acknowledge their worst moment, and rewards the Panel member who most disrupted the theory. Zero changes.

**The win condition itself (first to X):** Race-to-a-target is correct for this game. Timed-round formats (most points after N rounds) would require counting rounds and are worse for parties.

**Optional rules:** Hot Take Mode, Expert Mode, The Senate Hearing, Cinematic Universe Mode, Grand Unified Theory, The Deep State Ruling all kept. Grand Unified Theory cost reduced from 5 pts to 3 pts (5 pts was prohibitive at lower targets like 8–10 pts).

---

## Things Cut

**Public Discard (optional rule):** Absorbed into core rules as the default behavior.

**"2 minutes of silence" framing for PLAN phase:** Reframed as 60 seconds, explicitly used by the Panel to prepare questions. The silence was never the point.

**"First to vote BELIEVER and Theorist wins the round: +1 pt" Panel scoring:** This required tracking who voted first, which is impossible with simultaneous reveal. It was a rule that couldn't be executed as written. Cut.

**PLANT majority -1 pt for Theorist (charisma tax):** Kept but clarified as "more than half" to avoid ambiguity at odd Panel counts.

---

## Tone Notes

The v1 rulebook's voice was strong. v2 maintains it. The inline editorial comments (e.g., "Softball questions are a waste of everyone's time and you should be embarrassed") are intentional — they reinforce the game's personality and set expectations for new players without requiring separate example text.

---

## Playtesting Priorities for v2.0

1. Does 90-second Q&A feel too short at 10 players? (Floor Rule may need expansion to 2 vetoes.)
2. Does the written question requirement feel mandatory or annoying? (If annoying: make it encouraged, not required.)
3. Does 8 pts feel too easy at 9–10 players, or does it create the right drama?
4. Does the Chief Skeptic role improve or bog down 8+ player rounds?
5. Does THE LEAK +2 pt incentive make it feel strategic rather than random?

---

# v2.1 Changes

**Date:** 2026-02-22
**Scope:** Two targeted improvements: discard mechanics and Panel engagement during PLAN phase.

---

## Change 10: Shadow Evidence — Discards Become Active Weapons

**The problem (v2.0):** Discards are face-up, which is better than face-down, but still passive. They sit there. Panel members *can* reference them but rarely do under Q&A pressure. The mechanic was theoretical.

**The solution:** One Panel member per round may call **"SEIZED"** during PLAN phase to claim one discarded card as an interrogation weapon. This card goes face-down in front of them; during Interrogation they may reveal it as a formal challenge. The seizing Panel member alone judges satisfaction (same model as CITATION NEEDED).

**Scoring:** Theorist reconciles → +1 Theorist. Theorist fails → +1 Panel member. One challenge per round, first caller gets it.

**Why this works:**
- Creates immediate scarcity drama at the DRAW phase reveal — the moment discards flip face-up, Panel is scanning and racing to call seized
- Theorist now has a meta-reason to *not* discard obviously strong cards — or to discard a deliberately misleading one as a trap
- Adds genuine strategic depth without complexity (one mechanic, one resolution, clear judge)
- Consistent with the competitive market trend of emergent decisions from public information (Wavelength, Codenames, Spyfall)

**What happens to unseized discards?** They return **face-down to the bottom of their respective deck** at End of Turn. This:
- Prevents any discard pile buildup over a long game
- Means powerful cards cycle back into the deck and may reappear
- Eliminates the question of "when does the discard pile get reshuffled?"

---

## Change 11: Panel PLAN Phase — Three Concurrent Activities

**The problem (v2.0):** Writing one question is good but takes about 20 seconds. For the remaining 40 seconds, Panel members are watching the Theorist write silently. This is a partially solved downtime problem.

**The solution:** Three concurrent Panel activities, all optional except the written question:

1. **Write Your Question** — unchanged from v2.0, still required
2. **Shadow Evidence / SEIZED** — described above; 5-second decision
3. **Pre-Trial Wager** — privately predict your own vote (B/S/P) on the back of your Theory Sheet; +1 pt if it matches

**Pre-Trial Wager design rationale:**
- Takes 5 seconds to write. Zero explanation needed.
- Adds a second Panel scoring channel that rewards reading the theory cards before the presentation happens
- Creates a light "prediction game" layer: skilled players study the Theorist's chosen cards during PLAN and form an informed guess; casual players write randomly and occasionally get lucky
- Revealed during scoring creates a second beat of drama after the VOTE reveal ("Who was right about their own vote?")
- Borrowed from prediction mechanics in Camel Up and The Resistance — fast, personal, satisfying to resolve

**Combined effect of 3 activities:** The 60-second PLAN phase is now densely used. Panel members are: studying the theory cards, deciding whether to seize a discard, formulating a genuine question, and writing a private prediction. No one has idle hands.

---

## Playtesting Priorities for v2.1

1. Does "SEIZED" racing create fun urgency or awkward disputes? (May need a cleaner dispute rule — e.g., Panel member sitting closest to the discard pile wins, not "first to call")
2. Does Pre-Trial Wager feel like +1 free point (random guessing) or meaningful prediction? (If too random: restrict to only BELIEVER/PLANT, no SKEPTIC, making it a binary prediction)
3. Does the Shadow Evidence challenge actually get used? (If Panel forgets during Q&A pressure: add a reminder card for the seized player)
4. Does Theorist recycling unseized cards back to the deck change draw dynamics? (If decks run short: standard shuffle-discard rule kicks in)
