# Challenge: Print the first 10 Fibonacci numbers.

first = 0
second = 1

print(first, second, end=" ")
for _ in range(8):
    first, second = second, first + second
    print(second, end=" ")

print()
