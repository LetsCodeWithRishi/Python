# Challenge: Read a file safely and handle missing files.

filename = input("Enter filename: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("The file does not exist.")
