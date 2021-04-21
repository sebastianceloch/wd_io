def najwieksze(lista):
    lista.sort(reverse=True)
    return lista[:3]
lista=[1,4,3,6,4,8,9,5,3,4,5]
print(najwieksze(lista))
