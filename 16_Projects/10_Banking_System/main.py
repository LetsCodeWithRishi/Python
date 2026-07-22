"""A small banking simulation with guarded transactions."""


def main() -> None:
    balance = 0.0
    while True:
        command = input("[d]eposit, [w]ithdraw, [b]alance, [q]uit: ").strip().lower()
        if command == "b":
            print(f"Balance: {balance:.2f}")
        elif command in {"d", "w"}:
            try:
                amount = float(input("Amount: "))
                if amount <= 0:
                    raise ValueError
            except ValueError:
                print("Enter a positive number.")
                continue
            if command == "w" and amount > balance:
                print("Insufficient funds.")
            else:
                balance += amount if command == "d" else -amount
        elif command == "q":
            return
        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()
