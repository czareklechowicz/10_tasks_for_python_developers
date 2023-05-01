import statistics

numbers = input("Podaj listę liczb oddzielonych spacją: ").split()
numbers = [int(n) for n in numbers]

mean = sum(numbers) / len(numbers)

median = statistics.median(numbers)

print("Średnia arytmetyczna: ", mean)
print("Mediana: ", median)
