"""Record expenses and show a category summary."""
from collections import defaultdict


def main() -> None:
    expenses: dict[str, list[float]] = defaultdict(list)
    while True:
        category = input("Category (or 'done'): ").strip().title()
        if category.lower() == "done":
            break
        try:
            amount = float(input("Amount: "))
            if amount <= 0:
                raise ValueError
        except ValueError:
            print("Enter a positive number.")
            continue
        expenses[category].append(amount)
    for category, amounts in expenses.items():
        print(f"{category}: {sum(amounts):.2f}")
    print(f"Total: {sum(map(sum, expenses.values())):.2f}")


if __name__ == "__main__":
    main()
