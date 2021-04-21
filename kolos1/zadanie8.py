""" Napisz funkcję, która wczytuje z pliku zawierającego imiona i nazwiska studentów zapisane po jednym w linii, np.Marek Markowski
Paweł Budzikowski
Funkcja generuje dla podanej listy adresy e-mail postaci: imie.nazwisko@uwm.edu.pl i zapisuje dane do nowego pliku dopisując przy
wcześniejszym nazwisku wygenerowany adres, np.
Marek Markowski, marek.markowski@uwm.edu.pl itd. W nazwach e-mail powinny być zastępowane ewentualne polskie znaki (ż,ź
na z, ą na a itd.) """
def plik():
    with open("zadanie8.txt","r") as plik:
        dane = plik.readlines()
    plik.close()
    adres = '@uwm.edu.pl'
    list = [i.strip() for i in dane]
    for x in range(0,len(list)):
        list[x] = list[x].lower()
        list[x] = list[x].replace(' ','.')
        list[x] = list[x]+adres
        print(list[x])
    plik = open("zadanie8.txt","w+")
    for x in range(0,len(list)):
        plik.write(list[x]+"\n")
    plik.close()
plik()