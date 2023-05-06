liczby_str = input("Podaj listę liczb całkowitych, oddzielając je przecinkami: ")
liczby = [int(x.strip()) for x in liczby_str.split(",")]

for liczba in liczby:
    if liczba % 2 == 0:
        print(f"Liczba {liczba} jest parzysta")
    else:
        print(f"Liczba {liczba} jest nieparzysta")
