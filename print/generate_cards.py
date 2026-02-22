#!/usr/bin/env python3
"""WRGO Print & Play Generator
Produces a print-ready HTML file (2.5" x 3.5" poker cards, 9 per page).
Run: python3 generate_cards.py
Output: print-and-play.html
"""
import os

OUT = os.path.join(os.path.dirname(__file__), "print-and-play.html")

# ── Card data ─────────────────────────────────────────────────────────────────

DECK_A = [
    (1, "The Illuminati"), (2, "Big Pharma"), (3, "The Deep State"),
    (4, "Tech Billionaires"), (5, "NASA"), (6, "The Vatican"),
    (7, "Lizard People"), (8, "The CIA"), (9, "The World Economic Forum (WEF)"),
    (10, "Ancient Aliens"), (11, "The Freemasons"), (12, "The Rothschilds"),
    (13, "The Mainstream Media"), (14, "Big Oil"), (15, "Area 51 Scientists"),
    (16, "The Shadow Government"), (17, "The Global Elite"), (18, "Hollywood"),
    (19, "The New World Order"), (20, "Mark Zuckerberg"), (21, "Elon Musk"),
    (22, "Walt Disney (Cryogenically Frozen)"), (23, "The British Royal Family"),
    (24, "The Chinese Communist Party"), (25, "Central Banks / The Fed"),
    (26, "Secret Societies"), (27, "Climate Scientists"),
    (28, "The United Nations"), (29, "George Soros"), (30, "Bill Gates"),
    (31, "The Bilderberg Group"), (32, "Big Agriculture (Big Ag)"),
    (33, "The Military-Industrial Complex"), (34, "Rogue AI Systems"),
    (35, "Time Travelers from the Future"), (36, "The Pharmaceutical Cartel"),
    (37, "Ancient Sumerian Gods"), (38, "The Men in Black"), (39, "The 1%"),
    (40, "Social Media Algorithms"), (41, "Dark Web Operatives"),
    (42, "Space Force"), (43, "The Reptilian Bloodline"),
    (44, "Bohemian Grove Members"), (45, "The Trilateral Commission"),
    (46, "Big Tech Censors"), (47, "Off-World Colonists"),
    (48, "The Council of 13"), (49, "FEMA"),
    (50, "The Skull and Bones Society"),
]
DECK_A_WILD = [
    (51, "[YOUR CHOICE]", "Name any real or fictional actor of your choosing"),
    (52, "[YOUR CHOICE]", "Name any real or fictional actor of your choosing"),
    (53, "[COMBO]", "Play two Actor cards; both groups are working together"),
    (54, "[INSIDER]", "Your actor is a former member of the organization they're exposing"),
]

DECK_B = [
    (1, "faked the moon landing"),
    (2, "created COVID-19 in a lab"),
    (3, "is putting fluoride in the water to control our minds"),
    (4, "engineered the September 11th attacks"),
    (5, "controls the weather using HAARP technology"),
    (6, "built 5G towers to activate nanobots in the unvaccinated"),
    (7, "has been hiding free energy technology since the 1940s"),
    (8, "assassinated JFK — and framed Lee Harvey Oswald"),
    (9, "staged the bird flu pandemic"),
    (10, "replaced world leaders with clones"),
    (11, "is spraying chemtrails to suppress immune systems"),
    (12, "has been lying about the shape of the Earth"),
    (13, "is implanting tracking microchips through vaccines"),
    (14, "erased evidence of the Mandela Effect"),
    (15, "manufactured the 2008 financial crisis"),
    (16, "has been running a secret child trafficking network"),
    (17, "is suppressing a cancer cure discovered in 1972"),
    (18, "faked the deaths of multiple celebrities"),
    (19, "controls every major election worldwide"),
    (20, "is running the simulation we all live in"),
    (21, "built a secret base on the dark side of the Moon"),
    (22, "planned a 90% reduction in human population"),
    (23, "has been feeding us insect protein disguised as food"),
    (24, "is slowly replacing humans with AI replicas"),
    (25, "created the Great Reset as a cover for global takeover"),
    (26, "stages mass casualty events to push gun control"),
    (27, "communicates via frequencies hidden in pop music"),
    (28, "is tunneling under major cities through DUMB networks"),
    (29, "altered the historical timeline in 1963"),
    (30, "has been harvesting human consciousness for energy"),
    (31, "controls all mainstream search results globally"),
    (32, "engineered the Oklahoma City bombing as a false flag"),
    (33, "sabotaged cold fusion research in the 1980s"),
    (34, "is dosing the food supply with endocrine disruptors"),
    (35, "created the AIDS epidemic as a population control measure"),
    (36, "programmed financial crashes using algorithmic triggers"),
    (37, "faked the entire Apollo space program"),
    (38, "is mining rare minerals on the ocean floor and hiding it"),
    (39, "sabotaged Nikola Tesla's free energy experiments"),
    (40, "manufactured the 2020 election using postal ballot manipulation"),
    (41, "secretly controls all mainstream news outlets globally"),
    (42, "has been running a false flag alien disclosure operation"),
    (43, "is deploying AI censorship bots to suppress truth"),
    (44, "staged the Titanic sinking to eliminate political enemies"),
    (45, "created cryptocurrency to track all financial transactions"),
    (46, "has infiltrated every major university and corrupts research"),
    (47, "is building a global ID database through facial recognition"),
    (48, "engineered bird species extinction to replace them with drones"),
    (49, "is planning a staged alien invasion to consolidate power"),
    (50, "has been running a black-site human cloning program"),
]
DECK_B_WILD = [
    (51, "[YOUR CHOICE]", "Name any conspiracy act of your choosing"),
    (52, "[YOUR CHOICE]", "Name any conspiracy act of your choosing"),
    (53, "[ESCALATE]", "Your act is 10x bigger than any other player's; describe the full scale"),
    (54, "[ONGOING]", "This conspiracy has been happening since before recorded history"),
]

DECK_C = [
    (1, "to control the global population — and the Reddit thread proving it has been deleted three times"),
    (2, "because the Simpsons predicted it in 1998, down to the exact date"),
    (3, "and the proof is hidden in the murals at Denver International Airport"),
    (4, "to harvest adrenochrome from the general public"),
    (5, "because JFK Jr. revealed it in a coded QAnon drop"),
    (6, "to distract us from the truth about what's under Antarctica"),
    (7, "and the Georgia Guidestones spelled it out before they were demolished"),
    (8, "because the number 33 keeps appearing in every major news event"),
    (9, "to usher in the Great Reset and the digital prison state"),
    (10, "because birds aren't real — they're government surveillance drones"),
    (11, "using frequencies hidden in every major pop album since 1969"),
    (12, "because three whistleblowers confirmed it before disappearing"),
    (13, "to trigger a global economic collapse and buy assets at pennies"),
    (14, "and their own patent filings prove it if you know where to look"),
    (15, "to achieve immortality through methods we're not allowed to discuss"),
    (16, "because the mainstream media has actively refused to cover it"),
    (17, "to prepare Earth for the alien disclosure event scheduled for 2027"),
    (18, "because no one can actually explain the Baader-Meinhof phenomenon"),
    (19, "using satellites disguised as SpaceX Starlink launches"),
    (20, "because the Fibonacci sequence appears in every major disaster since 9/11"),
    (21, "to make humanity dependent on their pharmaceutical ecosystem forever"),
    (22, "and flat Earth maps reveal the geographic cover-up"),
    (23, "because internal documents were leaked on the dark web in 2019"),
    (24, "to terraform Earth for off-world colonists arriving within a decade"),
    (25, "using social media algorithms to bury any contradicting evidence"),
    (26, "because the original NASA footage was found in a New Zealand archive"),
    (27, "to consolidate all global financial power before the 2030 deadline"),
    (28, "and every fact-checker who investigates it gets immediately discredited"),
    (29, "because Nikola Tesla's suppressed patents clearly show the mechanism"),
    (30, "to force the population into a cashless, controllable digital economy"),
    (31, "because the Wayback Machine captured the deleted pages before the purge"),
    (32, "and the CIA's own declassified FOIA documents hint at it"),
    (33, "to install a one-world government before anyone notices"),
    (34, "because Gematria decoding of major news headlines confirms it"),
    (35, "using chemtrails to deliver the activating compound simultaneously"),
    (36, "because the moon's resonance frequency doesn't match a natural object"),
    (37, "to prevent the public from discovering zero-point energy"),
    (38, "and the Voynich Manuscript has been confirmed to contain the blueprint"),
    (39, "because former insiders posted coordinates on 4chan before being banned"),
    (40, "to use collective human fear as a psychic energy source"),
    (41, "because the missing 18 minutes of the Nixon tapes contained the proof"),
    (42, "using DARPA-funded deep fake technology to hide the evidence in plain sight"),
    (43, "because Area 51 flight logs obtained via FOIA show unexplained trips"),
    (44, "to ensure only the initiated survive the coming pole shift"),
    (45, "and predictive programming in blockbuster films has been softening us up"),
    (46, "because the book 'None Dare Call It Conspiracy' was pulled from every library"),
    (47, "to block humanity's spiritual awakening before the 2026 frequency shift"),
    (48, "using underwater cables that double as global mind-control antennas"),
    (49, "because the World Bank's own projections match the agenda timeline"),
    (50, "and three different astrologers independently predicted this exact moment"),
]
DECK_C_WILD = [
    (51, "[YOUR CHOICE]", "Name any motive or evidence of your choosing"),
    (52, "[YOUR CHOICE]", "Name any motive or evidence of your choosing"),
    (53, "[DOUBLE DOWN]", "Play two Evidence cards; your theory has twice the proof"),
    (54, "[PERSONAL WITNESS]", "You personally witnessed the evidence; describe what you saw"),
]

# Boost cards: (title, flavor, description)
BOOST_TYPES = [
    ("DOUBLE DOWN",
     "They're not just in on it. There's a layer above them.",
     "A second ACTOR is secretly controlling the first. Name the second actor during Q&amp;A and explain how they fit."),
    ("EXPERT WITNESS",
     "The credentials are real. The institution is also real. Neither of them exist.",
     "During Q&amp;A cite at least one fake expert by: full name, academic title, and institution. Make it convincing."),
    ("THE MEDIA COVERUP",
     "Whose side are you on, exactly?",
     "Every single answer during Q&amp;A must begin with the exact phrase: &ldquo;That's exactly what they want you to think.&rdquo; Forget once and lose the bonus."),
    ("CLASSIFIED FOOTAGE",
     "The proof exists. It's in this room. Right now.",
     "At some point during Q&amp;A, stand up, point to a specific location in the room, and explain what evidence would be found there."),
    ("TIMELINE SHIFT",
     "You think this started recently. Adorable.",
     "The conspiracy must now have begun at least 200 years earlier than originally implied. Explain the origins."),
    ("ALLY REVEALED",
     "One of you is not who they appear to be.",
     "Before Q&amp;A, secretly choose one Panel member. They are in on it. They must corroborate at least one answer unprompted. Both earn the bonus if successful."),
    ("IT'S BIGGER THAN YOU THINK",
     "You only scratched the surface.",
     "Draw one additional card from Deck B (THE ACT). This sub-conspiracy is also happening simultaneously. Incorporate it into your answers."),
    ("THEY'RE IN THIS ROOM",
     "Look around you.",
     "At some point during Q&amp;A, imply (do not accuse directly) that one questioner is an operative of the conspiracy. Do not name them."),
    ("THE ACCIDENTAL CONFESSION",
     "You weren't supposed to say that. You definitely didn't say that.",
     "Accidentally reveal something alarming mid-answer, then immediately attempt to walk it back. Example: &ldquo;...and the second phase begins in March— I didn't say that.&rdquo;"),
    ("NOTHING TO SEE HERE",
     "That question is classified. For your own safety.",
     "Refuse to answer exactly one question during Q&amp;A. Explain calmly why answering would be dangerous. One use only."),
]

THE_LEAK = (
    "THE LEAK",
    "Somewhere in this deck is something they slipped in.",
    "Write a note on Theory Sheet paper. Secretly pass it to any Panel member. They must read it aloud during Q&amp;A as if receiving a genuine anonymous tip. Content is your choice."
)


# ── Helpers ───────────────────────────────────────────────────────────────────

def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&#39;")

def text_cls(text):
    n = len(text)
    if n <= 22: return ""
    if n <= 38: return " med"
    if n <= 58: return " sm"
    return " xs"


# ── Card HTML builders ────────────────────────────────────────────────────────

def std_card(num, text, deck_cls, hdr, qlabel):
    t = esc(text)
    sz = text_cls(t)
    return (
        f'<div class="c {deck_cls}">'
        f'<div class="h"><span class="dl">{hdr}</span><span class="n">{num}</span></div>'
        f'<div class="b"><div class="q">{qlabel}</div><div class="t{sz}">{t}</div></div>'
        f'<div class="f">WRGO</div>'
        f'</div>\n'
    )

def wild_card(num, title, sub, deck_cls, hdr, qlabel):
    return (
        f'<div class="c {deck_cls} wc">'
        f'<div class="h"><span class="dl">{hdr} &mdash; WILD</span><span class="n">{num}</span></div>'
        f'<div class="b">'
        f'<div class="q">{qlabel}</div>'
        f'<div class="t med">[{esc(title)}]</div>'
        f'<div class="sub">{esc(sub)}</div>'
        f'</div>'
        f'<div class="f">WRGO</div>'
        f'</div>\n'
    )

def boost_card(card_num, title, flavor, desc, is_leak=False, copy_label=""):
    extra = " leak" if is_leak else ""
    cl = "" if copy_label == "" else f'<div class="bcopy">{copy_label}</div>'
    return (
        f'<div class="c d bc{extra}">'
        f'<div class="h"><span class="dl">{"THE LEAK" if is_leak else "BOOST"}</span><span class="n">{card_num}</span></div>'
        f'<div class="b">'
        f'<div class="btitle">{title}</div>'
        f'<div class="bflavor">{flavor}</div>'
        f'<div class="bdesc">{desc}</div>'
        f'{cl}'
        f'</div>'
        f'<div class="f">WRGO</div>'
        f'</div>\n'
    )


# ── CSS ───────────────────────────────────────────────────────────────────────

CSS = """
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: Georgia, serif; background: #fff; color: #111; }

/* Screen-only elements */
.guide {
  max-width: 7.5in; margin: 0.3in auto 0.1in; padding: 10px 14px;
  background: #fffde7; border: 1px solid #f9a825; border-radius: 4px;
  font-family: Arial, sans-serif; font-size: 9pt; line-height: 1.6;
}
.guide strong { display: block; margin-bottom: 4px; font-size: 10pt; }
.dlabel {
  max-width: 7.5in; margin: 0.15in auto 0.05in;
  font-family: Arial, sans-serif; font-size: 11pt; font-weight: bold; color: #666;
  padding-left: 2px;
}
@media print { .guide, .dlabel { display: none; } }

/* Card grid — 3×3, letter paper */
.grid { width: 7.5in; margin: 0 auto; display: flex; flex-wrap: wrap; }
.newdeck { page-break-before: always; break-before: page; }

/* Base card */
.c {
  width: 2.5in; height: 3.5in;
  border: 1px dashed #bbb;
  display: flex; flex-direction: column;
  overflow: hidden;
  page-break-inside: avoid; break-inside: avoid;
  -webkit-print-color-adjust: exact; print-color-adjust: exact;
}

/* Header band */
.h {
  padding: 5px 7px; display: flex;
  justify-content: space-between; align-items: center;
  flex-shrink: 0;
}
.h .dl { font-family: Arial, sans-serif; font-size: 6pt; font-weight: bold;
  letter-spacing: 1.5px; text-transform: uppercase; color: rgba(255,255,255,.85); }
.h .n  { font-family: Arial, sans-serif; font-size: 6pt; color: rgba(255,255,255,.6); }

/* Card body */
.b {
  flex: 1; display: flex; flex-direction: column;
  align-items: center; justify-content: center;
  padding: 0.1in 0.12in; text-align: center;
}
.b .q { font-family: Arial, sans-serif; font-size: 6pt; text-transform: uppercase;
  letter-spacing: 2px; color: #ccc; margin-bottom: 7px; }
.b .t      { font-size: 14pt; font-weight: bold; line-height: 1.3; }
.b .t.med  { font-size: 12pt; }
.b .t.sm   { font-size: 9.5pt; }
.b .t.xs   { font-size: 8pt; }
.b .sub    { font-family: Arial, sans-serif; font-size: 7pt; color: #777;
  margin-top: 8px; line-height: 1.4; font-style: italic; }

/* Boost card overrides */
.bc .b { padding: 0.08in 0.12in; }
.bc .b .btitle { font-family: Arial, sans-serif; font-size: 14pt; font-weight: bold;
  color: #111; margin-bottom: 3px; }
.bc .b .bflavor { font-family: Arial, sans-serif; font-size: 6.5pt; font-style: italic;
  color: #999; margin-bottom: 6px; line-height: 1.3; }
.bc .b .bdesc  { font-family: Arial, sans-serif; font-size: 7.5pt; color: #333;
  line-height: 1.45; text-align: left; }
.bc .b .bcopy  { font-family: Arial, sans-serif; font-size: 5.5pt; color: #bbb;
  margin-top: 5px; letter-spacing: 1px; }

/* Footer */
.f { text-align: center; font-family: Arial, sans-serif; font-size: 5pt;
  color: #ccc; letter-spacing: 2px; text-transform: uppercase;
  padding: 2px 0; border-top: 1px solid #f0f0f0; flex-shrink: 0; }

/* Deck colours */
.a .h         { background: #c0392b; }
.a.wc .h      { background: #7b241c; }
.b_ .h        { background: #1c2833; }
.b_.wc .h     { background: #0d1117; }
.cc .h        { background: #1e8449; }
.cc.wc .h     { background: #145a32; }
.d .h         { background: #6c3483; }
.d.bc.leak .h { background: #1b2631; }
"""


# ── HTML template ─────────────────────────────────────────────────────────────

def build_html(body):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>What's Really Going On — Print &amp; Play</title>
<style>{CSS}</style>
</head>
<body>

<div class="guide">
  <strong>WRGO — Print &amp; Play Instructions</strong>
  Print on <b>letter-size paper (8.5&Prime; &times; 11&Prime;)</b> at <b>100% / Actual size</b> — do NOT scale to fit.
  Each page = 9 cards (3&times;3). Cut along dashed lines.
  Recommended: <b>110 lb cardstock</b>. Optional: sleeve in standard poker sleeves (2.5&Prime; &times; 3.5&Prime;).<br>
  Decks: <b style="color:#c0392b">A — WHO (Red, 54 cards)</b> &nbsp;|&nbsp;
         <b>B — WHAT (Black, 54 cards)</b> &nbsp;|&nbsp;
         <b style="color:#1e8449">C — WHY/HOW (Green, 54 cards)</b> &nbsp;|&nbsp;
         <b style="color:#6c3483">D — BOOST (Purple, 31 cards)</b>
</div>

{body}

</body>
</html>
"""


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    sections = []

    # ── DECK A ──
    sections.append('<div class="dlabel">DECK A — THE ACTORS (WHO) &nbsp;&bull;&nbsp; Red &nbsp;&bull;&nbsp; 54 cards</div>\n<div class="grid">\n')
    for num, text in DECK_A:
        sections.append(std_card(num, text, "a", "DECK A — WHO", "WHO"))
    for num, title, sub in DECK_A_WILD:
        sections.append(wild_card(num, title, sub, "a", "DECK A — WHO", "WHO"))
    sections.append("</div>\n")

    # ── DECK B ──
    sections.append('<div class="dlabel newdeck">DECK B — THE ACT (WHAT) &nbsp;&bull;&nbsp; Black &nbsp;&bull;&nbsp; 54 cards</div>\n<div class="grid newdeck">\n')
    for num, text in DECK_B:
        sections.append(std_card(num, text, "b_", "DECK B — WHAT", "WHAT"))
    for num, title, sub in DECK_B_WILD:
        sections.append(wild_card(num, title, sub, "b_", "DECK B — WHAT", "WHAT"))
    sections.append("</div>\n")

    # ── DECK C ──
    sections.append('<div class="dlabel newdeck">DECK C — THE EVIDENCE (WHY/HOW) &nbsp;&bull;&nbsp; Green &nbsp;&bull;&nbsp; 54 cards</div>\n<div class="grid newdeck">\n')
    for num, text in DECK_C:
        sections.append(std_card(num, text, "cc", "DECK C — WHY/HOW", "WHY / HOW"))
    for num, title, sub in DECK_C_WILD:
        sections.append(wild_card(num, title, sub, "cc", "DECK C — WHY/HOW", "WHY / HOW"))
    sections.append("</div>\n")

    # ── DECK D (Boost) ──
    sections.append('<div class="dlabel newdeck">DECK D — CONSPIRACY BOOST &nbsp;&bull;&nbsp; Purple &nbsp;&bull;&nbsp; 31 cards</div>\n<div class="grid newdeck">\n')
    card_num = 1
    for i, (title, flavor, desc) in enumerate(BOOST_TYPES, 1):
        for copy in range(1, 4):
            sections.append(boost_card(card_num, title, flavor, desc, copy_label=f"Copy {copy} of 3"))
            card_num += 1
    # THE LEAK
    title, flavor, desc = THE_LEAK
    sections.append(boost_card(card_num, title, flavor, desc, is_leak=True))
    sections.append("</div>\n")

    html = build_html("".join(sections))
    with open(OUT, "w") as f:
        f.write(html)
    print(f"Written: {OUT}")
    total_cards = len(DECK_A) + len(DECK_A_WILD) + len(DECK_B) + len(DECK_B_WILD) + len(DECK_C) + len(DECK_C_WILD) + (len(BOOST_TYPES) * 3) + 1
    print(f"Total cards: {total_cards}")


if __name__ == "__main__":
    main()
