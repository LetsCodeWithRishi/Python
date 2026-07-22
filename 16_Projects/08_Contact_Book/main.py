"""An in-memory contact book."""


def main() -> None:
    contacts: dict[str, str] = {}
    while True:
        command = input("[a]dd, [f]ind, [l]ist, [q]uit: ").strip().lower()
        if command == "a":
            name = input("Name: ").strip()
            phone = input("Phone: ").strip()
            if name and phone:
                contacts[name] = phone
        elif command == "f":
            print(contacts.get(input("Name: ").strip(), "Contact not found."))
        elif command == "l":
            for name, phone in sorted(contacts.items()):
                print(f"{name}: {phone}")
        elif command == "q":
            return
        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()
