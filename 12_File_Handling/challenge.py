# Challenge: Save a student's name and age to a file.

name = input("Enter student name: ")
age = input("Enter student age: ")

with open("student.txt", "w", encoding="utf-8") as file:
    file.write(f"Name: {name}\nAge: {age}")

print("Student information saved.")
