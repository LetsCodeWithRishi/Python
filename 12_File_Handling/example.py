filename = "sample.txt"
with open(filename, "w", encoding="utf-8") as file:
    file.write("Hello from Python")

with open(filename, "r", encoding="utf-8") as file:
    print(file.read())
