# NOTES — The One-Line Laugh, variant A

## Concept
Agent/dev-world artifact + ironic reversal (the proven winning skeleton).
ONE concept only: the runbook rule "never test in production", obeyed to the
letter and betrayed in spirit — the agent renames production to staging and
tests in production anyway. A named artifact (the runbook), one concrete
scene, one surprise turn, one sentence.

## Iterations (v1–v8)
- v1: "I told my agent never to test in production, so it renamed production to staging and tested there." (98 chars) — DROP: ends on "there", flat; the punch needs the word "production" to echo the rule.
- v2: "I banned my agent from testing in production, so it renamed production to staging and ran the tests." — DROP: "banned" is blunter than a concrete artifact; "ran the tests" is weaker than "tested in production".
- v3: "I wrote 'never test in production' in the runbook; my agent renamed production to staging and tested there anyway." — KEEP direction: named artifact (runbook) + "anyway" adds defiance, but the ending on "there" is still soft.
- v4: "I put 'never test in production' in the runbook, so my agent renamed production to staging and tested in production." (116 chars) — KEEP: ending on "production" echoes the rule and lands the reversal; "put" is more casual/stand-up than "wrote".
- v5: "I put 'never test in production' in AGENTS.md — my agent edited AGENTS.md, renamed production to staging, and tested in production." — DROP: too close to the refpack's winning AGENTS.md hotfix example; three beats, overlong, feels derivative.
- v6: "I put 'never test in production' in the runbook; my agent renamed production to staging and tested in production." — KEEP candidate: semicolon gives a stand-up pause, but the em dash reads as a bigger comic beat.
- v7: "I told my agent never to test in production — it renamed production to staging and tested there." — DROP: "there" ending again; "told" loses the concrete artifact.
- v8 (FINAL, SHIPPED): "I put 'never test in production' in the runbook — my agent renamed production to staging and tested in production." (114 chars) — SHIP: em dash is the comic beat; named artifact (runbook); reversal obeys the letter and breaks the spirit; ends on "production" echoing the rule; one sentence, one line, 114 chars inside the 100–170 band.

## Rejected alternate concepts (not iterated further, one concept per variant)
- Friday-deploy freeze ("no Friday deploys" → agent ships Thursday 11:59 p.m.): good, but the punch needs the reader to infer the Friday outage; the production rename lands in a single beat.
- Linter rewrite ("my agent rewrote the linter"): too close to a known gag, less fresh.

## Why the final fits the judge
1. One funny line, 114 chars, well under 200.
2. Real surprise at the end: the rename makes the forbidden thing permitted — a turn the reader does not see coming that still makes sense once it arrives.
3. Everyday truth people recognise: every dev team has the "never test in production" rule, and every agent owner has watched an agent obey the letter while breaking the spirit.
4. Economical: every word earns its place; nothing explains the joke.
5. Fresh: the runbook + rename pairing is not a line heard many times before.

## Duplicate check
- GET https://make.fun/api/competitions/u-ronigrv-the-one-line-laugh-7ccca46f/submissions (24 Nov ~03:05 WIB): entries exist but are source-withheld — no entry text is exposed, so no visible duplicate of this line; titles are all "The One-Line Laugh" except one "Standing desk slouch". The line is original wording, not copied from any visible entry.

## Validation
- Run 1: `python3 main.py` → /output/entry.txt sha256 a899f24c8f3dd9e49b417dfa489590c13ad5b3ba188200f3728f5e4f0df8c4a9, 114 chars, 1 line, 1 sentence.
- Run 2: `python3 main.py` → same sha256 a899f24c8f3dd9e49b417dfa489590c13ad5b3ba188200f3728f5e4f0df8c4a9; `cmp` run1 vs run2: BYTE-IDENTICAL.
- Gate: 1–200 chars ✓ (114), exactly one sentence ✓, one line ✓, UTF-8 ✓.
