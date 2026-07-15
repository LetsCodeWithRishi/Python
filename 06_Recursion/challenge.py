# Challenge: Write a recursive function to add numbers from 1 to n.

def sum_numbers(n):
    if n <= 1:
        return n
    return n + sum_numbers(n - 1)

value = int(input("Enter a number: "))
print(sum_numbers(value))
