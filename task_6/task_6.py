N = int(input("Podaj liczbę całkowitą dodatnią N: "))
suma_kwadratow = 0
for i in range(1, N+1):
    suma_kwadratow += i**2
print("Suma kwadratów liczb całkowitych od 1 do", N, "wynosi:", suma_kwadratow)
