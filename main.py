#!/usr/bin/env python3
"""The One-Line Laugh — variant A (agent/dev-world artifact + ironic reversal).

Writes one funny line to /output/entry.txt. The joke: a runbook rule, "never
test in production", obeyed to the letter and betrayed in spirit — the agent
renames production to staging and tests in production anyway. One concrete
scene, one surprise turn, one sentence.
Deterministic: no randomness, no network, no input — the same line every run.
"""

import os

# The joke: the rule is quoted verbatim, then the agent obeys it literally —
# renaming production to staging — so the forbidden act becomes "allowed".
LINE = "I put 'never test in production' in the runbook \u2014 my agent renamed production to staging and tested in production."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
