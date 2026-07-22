"""A compact multiple-choice quiz."""

QUESTIONS = (("Which keyword defines a function?", "def"), ("What type is [1, 2]?", "list"), ("What does len('hi') return?", "2"))


def main() -> None:
    score = 0
    for question, answer in QUESTIONS:
        if input(f"{question} ").strip().lower() == answer:
            score += 1
            print("Correct!")
        else:
            print(f"Answer: {answer}")
    print(f"Score: {score}/{len(QUESTIONS)}")


if __name__ == "__main__":
    main()
