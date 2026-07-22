"""Iterate with for and while, and control a loop with continue and break."""

for number in range(1, 6):
    if number == 3:
        continue
    print(f"for loop: {number}")

count = 0
while True:
    count += 1
    print(f"while loop: {count}")
    if count == 3:
        break
