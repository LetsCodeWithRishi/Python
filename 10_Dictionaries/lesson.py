"""Dictionaries map unique keys to values."""

student = {"name": "Riya", "age": 21, "marks": {"math": 90, "science": 88}}
student["age"] += 1
for subject, mark in student["marks"].items():
    print(f"{student['name']} — {subject}: {mark}")
