""" Wygeneruj macierz (lista wielopoziomowa, nie tablica numpy) 5x5 wypełnioną wartościami losowymi z przedziału 1-10. Wyświetl
sumę wartości w 2 kolumnie. """
import random
num = [random.randint(1,10) for i in range(1,26,1)]
macierz = [num[i * 5:i * 5 + 5] for i in range(int(len(num) /5 ))]
print(macierz)
for i in range(0,5,1):
    print(macierz[i][1])