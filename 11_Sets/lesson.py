"""Sets contain unique, unordered values and support set algebra."""

python_students = {"Asha", "Dev", "Riya"}
math_students = {"Dev", "Riya", "Sam"}
print(f"both={python_students & math_students}")
print(f"either={python_students | math_students}")
