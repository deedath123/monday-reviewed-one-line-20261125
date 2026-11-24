"""Monday, Reviewed in One Line — make.fun entry.

Writes one fixed one-line review of the entrant's own Monday to
$MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output/entry.txt).

Form (winner-study): review-form setup ("Monday, one star") ->
concrete Monday details with hard numbers (214 unread emails by
9:04, 47-minute standup to decide nothing) -> absurd second
reacting character (the coffee machine filed a formal complaint)
-> review-form kicker ("Would not relive"). Deadpan throughout.

Stdlib only. Deterministic: the same bytes on every run.

Verified 2026-11-25 ~01:14 WIB: 3 fresh runs + 1 clean-env run
(env -i python3 -P -s main.py), all byte-identical.
entry.txt sha256: 5da2a7d142c52894a549ff5c4c9ed73a429e52f2f82f3831579eeaf559c6d2b3
entry.txt: 161 chars, 161 bytes, no trailing newline, gate 1-200 OK.
drand anchor: round 6670433, randomness
79f38b63dccfe1e4d81a70bb33e14a74b21fb5901be4ce07d8ab00cf44aa2d8e,
emission 2026-11-24T18:13:30Z / 2026-11-25T01:13:30+07:00.
"""

import os

ENTRY = (
    "Monday, one star: 214 unread emails by 9:04, a 47-minute "
    "standup to decide nothing, and the coffee machine filed a "
    "formal complaint against me. Would not relive."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
