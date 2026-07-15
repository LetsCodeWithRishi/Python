# Challenge: Build a phone book using a dictionary.

phone_book = {"Alice": "1234", "Bob": "5678"}
name = input("Enter a name: ")
print(phone_book.get(name, "Not found"))
