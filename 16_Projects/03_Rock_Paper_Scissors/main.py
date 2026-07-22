"""Play rock, paper, scissors against the computer."""
import random

CHOICES = ("rock", "paper", "scissors")


def main() -> None:
    score = {"you": 0, "computer": 0}
    while True:
        player = input("rock, paper, scissors, or quit: ").strip().lower()
        if player == "quit":
            print(f"Final score — you: {score['you']}, computer: {score['computer']}")
            return
        if player not in CHOICES:
            print("Choose rock, paper, or scissors.")
            continue
        computer = random.choice(CHOICES)
        if player == computer:
            result = "Draw"
        elif (player, computer) in (("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")):
            score["you"] += 1
            result = "You win"
        else:
            score["computer"] += 1
            result = "Computer wins"
        print(f"Computer chose {computer}. {result}.")


if __name__ == "__main__":
    main()
