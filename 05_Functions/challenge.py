# Challenge: Create a function that checks whether a number is prime.

def is_prime(number):
    if number <= 1:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True

value = int(input("Enter a number: "))
print(is_prime(value))
