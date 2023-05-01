text = input("Podaj napis: ")

letter_count = {}

for letter in text.lower():
    if letter.isalpha():
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

for letter, number in letter_count.items():
    print(f"{letter}: {number}")
