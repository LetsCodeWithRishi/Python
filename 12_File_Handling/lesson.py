"""Read and write files relative to this lesson, not the current shell folder."""
from pathlib import Path

DATA_FILE = Path(__file__).with_name("sample.txt")

DATA_FILE.write_text("first line\n", encoding="utf-8")
with DATA_FILE.open("a", encoding="utf-8") as file:
    file.write("second line\n")
print(DATA_FILE.read_text(encoding="utf-8"))
