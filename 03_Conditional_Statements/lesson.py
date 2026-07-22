"""Use if, elif, and else to select program behaviour."""

def grade(mark: int) -> str:
    if not 0 <= mark <= 100:
        raise ValueError("Mark must be between 0 and 100.")
    if mark >= 90:
        return "A"
    if mark >= 75:
        return "B"
    if mark >= 50:
        return "C"
    return "D"


for mark in (92, 81, 65, 42):
    print(f"{mark}: {grade(mark)}")
