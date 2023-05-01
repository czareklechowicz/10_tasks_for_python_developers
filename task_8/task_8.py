text = input("Podaj ciąg znaków: ")
reverse_text = ""

for i in range(len(text)-1, -1, -1):
    reverse_text += text[i]

print("Ciąg znaków od tyłu:", reverse_text)
