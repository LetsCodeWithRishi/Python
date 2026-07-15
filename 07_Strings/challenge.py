# Challenge: Count vowels in a sentence.

text = input("Enter a sentence: ").lower()
vowels = "aeiou"
count = sum(1 for char in text if char in vowels)
print(f"Vowel count: {count}")
