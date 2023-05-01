number_str = input("Podaj listę liczb całkowitych, oddzielając je przecinkami: ")
number = [int(x.strip()) for x in number_str.split(",")]

average = sum(number) / len(number)
sum = sum(number)
minimum = min(number)
maximum = max(number)

print(f"Suma: {sum}")
print(f"Średnia arytmetyczna: {average}")
print(f"Największa liczba: {maximum}")
print(f"Najmniejsza liczba: {minimum}")
