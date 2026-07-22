"""Tuples are ordered, immutable records that support unpacking."""

person = ("Amit", 25, "India")
name, age, country = person
scores = (78, 85, 85, 90)
print(f"{name} ({age}) from {country}; 85 occurs {scores.count(85)} times")
