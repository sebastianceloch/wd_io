""" Korzystając z Python comprehensions wygeneruj listę 10 elementów postaci _O_, _OO_ ( litera ‘O’ oraz podkreślenie) itd. """
lista = ["_"+"O"*x+"_" for x in range(1,11,1)]
print(lista)