"""Index, slice, transform, and format immutable text."""

text = "  Python programming  "
clean = text.strip()
print(f"first={clean[0]!r}, slice={clean[:6]!r}, words={clean.split()}")
print(f"upper={clean.upper()}; length={len(clean)}")
