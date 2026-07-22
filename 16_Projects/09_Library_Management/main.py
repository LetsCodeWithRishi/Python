"""Track a small library's available books."""


def main() -> None:
    available = {"Python Crash Course", "Clean Code", "The Pragmatic Programmer"}
    borrowed: set[str] = set()
    while True:
        command = input("[l]ist, [b]orrow, [r]eturn, [q]uit: ").strip().lower()
        if command == "l":
            print("Available:\n" + "\n".join(sorted(available)))
        elif command == "b":
            title = input("Title: ").strip()
            if title in available:
                available.remove(title)
                borrowed.add(title)
                print("Borrowed.")
            else:
                print("Book unavailable.")
        elif command == "r":
            title = input("Title: ").strip()
            if title in borrowed:
                borrowed.remove(title)
                available.add(title)
                print("Returned.")
            else:
                print("That book was not borrowed.")
        elif command == "q":
            return
        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()
