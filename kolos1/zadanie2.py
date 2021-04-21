""" Napisz funkcję, która na podstawie listy liczb całkowitych jako parametr wejściowy będzie zwracała wartość ze środka listy, jeżeli ich
liczba będzie nieparzysta lub średnią z dwóch wartości środkowych jeżeli ich liczba jest parzysta. Lista powinna być posortowana
rosnąco. """
def list(lista):
    a=len(lista)
    pom=a/2
    if(a%2==1):
        return lista[int(pom)]
    elif(a%2==0):
        pom2 = lista[int(pom)]+lista[int(pom)-1]/2
        return pom2
lista = [1,2,3,4,15,6]
lista.sort()
print(list(lista))