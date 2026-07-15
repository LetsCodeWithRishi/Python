# Example: a tiny calculator menu for a beginner project.

print("Simple Calculator")
print("1. Add")
print("2. Subtract")

choice = input("Choose an option: ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == "1":
    print("Result:", num1 + num2)
elif choice == "2":
    print("Result:", num1 - num2)
else:
    print("Invalid option")
