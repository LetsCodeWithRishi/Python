"""Generate a secure password using the standard library."""
import secrets
import string


def main() -> None:
    try:
        length = int(input("Password length (12 or more): "))
        if length < 12:
            raise ValueError
    except ValueError:
        print("Choose a whole number of at least 12.")
        return
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(alphabet) for _ in range(length))
    print(f"Password: {password}")


if __name__ == "__main__":
    main()
