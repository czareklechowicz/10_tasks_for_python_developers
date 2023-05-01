user_input = input("Wpisz imiona z wielkiej litery oddzielając je przecinkami:")
names = [x.strip() for x in user_input.split(",")]

names_with_a = []
for name in names:
    if name.startswith('A'):
        names_with_a.append(name)


print("Imiona zaczynające się na literę A to:", names_with_a)