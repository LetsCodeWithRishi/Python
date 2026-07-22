"""Recursive functions must have a base case and make progress toward it."""


def factorial(number: int) -> int:
    if number < 0:
        raise ValueError("Factorial is undefined for negative numbers.")
    return 1 if number < 2 else number * factorial(number - 1)


def is_palindrome(text: str) -> bool:
    return len(text) < 2 or (text[0] == text[-1] and is_palindrome(text[1:-1]))


print(factorial(5))
print(is_palindrome("level"))
