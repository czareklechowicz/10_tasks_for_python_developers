strings = input("Podaj listę napisów oddzielonych spacją: ").split()

for string in sorted(strings):
    print(f"{string}: {len(string)}")
