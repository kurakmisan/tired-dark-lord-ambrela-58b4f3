"""The Tired Dark Lord: A 100-Word Villain Monologue.

Writes one original monologue (~100 words) to /output/entry.txt.

The speaker is a specific villain: a dark lord besieging the same small
city for the seventh time, with a scheme (the slow conquest) and a history
(six earlier sieges, dragons, a prophecy). His tiredness is never announced:
it lives in the rhythm, the pauses, the forgotten list, the bad back, and
the decision to finish the conquest sitting down.

Deterministic: no input, no network, no randomness. Pure stdlib.
"""

import os

TEXT = (
    "This is the seventh time I've besieged your little city, boy, and here's "
    "what I've learned: your innkeeper makes a better stew than my entire war "
    "council. I used to arrive with dragons. Now it's a bad back and a list I "
    "keep forgetting halfway through, what was I saying? The prophecy says "
    "I will drown the valley in fire. The prophecy never mentioned the stairs. "
    "So I'll sit here, outside your walls, and wait. Cities surrender "
    "eventually \u2014 to hunger, to boredom, to pity. Mine is the slowest "
    "conquest in history, and the only one I'll finish sitting down."
)


def main() -> None:
    # Gate guard: the sealed scorer accepts 1-600 UTF-8 characters, and the
    # brief asks for about 100 words. Fail loudly instead of writing a text
    # that could never be judged.
    words = TEXT.split()
    if not 90 <= len(words) <= 110:
        raise SystemExit(f"word count out of range: {len(words)}")
    if not 1 <= len(TEXT) <= 600:
        raise SystemExit(f"character count out of range: {len(TEXT)}")
    if "\n" in TEXT or "\r" in TEXT:
        raise SystemExit("entry must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
