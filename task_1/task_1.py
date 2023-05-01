with open('dane.txt', 'r') as f:
    dane = f.readlines()
liczby = []

for d in dane:
    liczby.append(int(d.strip()))

liczby.sort(reverse=True)
three_biggest = liczby[:3]

print(three_biggest)
