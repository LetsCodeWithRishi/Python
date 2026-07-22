"""Guess a randomly selected number."""
import random


def main() -> None:
    target = random.randint(1, 100)
    attempts = 0
    print("Guess the number from 1 to 100.")
    while True:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Enter a whole number.")
            continue
        attempts += 1
        if guess < target:
            print("Too low.")
        elif guess > target:
            print("Too high.")
        else:
            print(f"Correct in {attempts} attempts!")
            return


if __name__ == "__main__":
    main()
