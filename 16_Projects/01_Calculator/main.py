"""A four-operation calculator with input validation."""


def read_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Enter a valid number.")


def main() -> None:
    operations = {"+": lambda a, b: a + b, "-": lambda a, b: a - b,
                  "*": lambda a, b: a * b, "/": lambda a, b: a / b}
    first = read_number("First number: ")
    operator = input("Operator (+, -, *, /): ").strip()
    second = read_number("Second number: ")
    if operator not in operations:
        print("Unsupported operator.")
    elif operator == "/" and second == 0:
        print("Cannot divide by zero.")
    else:
        print(f"Result: {operations[operator](first, second):g}")


if __name__ == "__main__":
    main()
