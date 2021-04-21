""" Napisz funkcję, która przyjmuje listę plików jako argument wejściowy, i zapisuje ich zawartość do jednego pliku (dowolna nazwa
pliku wyjściowego) """
def plik(lista):
    plik = open("plik.txt","w")
    for x in range(0,len(lista)):
        plik.write(str(lista[x]))
        plik.write("\n")
    plik.close()
lista=["text.txt","tekst.txt","write.txt"]
plik(lista)
