"""Write the entry chill for make.fun's "One Line, One Chill" bounty.

The entry is one line of horror, under 200 characters: a single
sentence that frightens in one breath, no setup, no second sentence,
just the moment the room goes wrong — a voice that should not be
there, speaking in a voice that should be yours. The program checks
the line really is one sentence: exactly one period, at the end.
This program writes that line to entry.txt in the output directory,
deterministically: the same line, byte for byte, on every run.
Standard library only; no network.
"""

import os

LINE = "The smart speaker in the empty house said goodnight in my voice before I had spoken a word."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DESTINATION = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    if not 1 <= len(LINE) <= 200:
        raise ValueError("line must be 1 to 200 characters")
    if not LINE.strip():
        raise ValueError("line must not be only whitespace")
    if LINE.count(".") != 1 or not LINE.endswith("."):
        raise ValueError("entry must be a single sentence")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Do not chmod the output directory: the grader runs this program
    # as a different user on a directory it does not own, and chmod
    # would fail the run. The file we create gets mode 0644 below,
    # which is all make.fun needs to collect it.
    with open(DESTINATION, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    os.chmod(DESTINATION, 0o644)
    print("wrote {} ({} characters)".format(DESTINATION, len(LINE)))


if __name__ == "__main__":
    main()
