"""A simple in-memory task manager."""


def main() -> None:
    tasks: list[str] = []
    while True:
        command = input("[a]dd, [l]ist, [r]emove, [q]uit: ").strip().lower()
        if command == "a":
            task = input("Task: ").strip()
            if task:
                tasks.append(task)
        elif command == "l":
            print("\n".join(f"{index}. {task}" for index, task in enumerate(tasks, 1)) or "No tasks.")
        elif command == "r":
            try:
                print(f"Removed: {tasks.pop(int(input('Task number: ')) - 1)}")
            except (ValueError, IndexError):
                print("That task does not exist.")
        elif command == "q":
            return
        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()
