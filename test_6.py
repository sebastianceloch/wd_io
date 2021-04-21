def plik():
    with open("plik.txt","r") as plik:
        dane = plik.readlines()
    lista = [int(x.strip()) for x in dane]
    lista.sort()
    plik.close()
    plik = open("plik.txt","w")
    for x in range(0,len(lista)):
        plik.write(str(lista[x]))
        plik.write("\n")
    plik.close()
plik()
