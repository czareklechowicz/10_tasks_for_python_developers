list = input("Podaj listę liczb oddzielonych spacją: ").split()
after_list = []

for number in list:
    if int(number) % 3 == 0 or int(number) % 5 == 0:
        after_list.append(number)

print("Liczby z twojej listy podzielne przez 3 lub 5 to:", ' '.join(after_list))
