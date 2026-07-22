"""Catch expected errors narrowly and use finally for required cleanup."""


class InvalidAgeError(ValueError):
    """Raised when an age is outside the accepted range."""


def parse_age(value: str) -> int:
    age = int(value)
    if not 0 <= age <= 130:
        raise InvalidAgeError("Age must be between 0 and 130.")
    return age


try:
    print(parse_age("21"))
except ValueError as error:
    print(f"Input error: {error}")
finally:
    print("Validation finished.")
