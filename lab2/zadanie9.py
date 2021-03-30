liczba = input("podaj liczbe wielocyfrowa ")
suma = 0
pom=0
x=len(liczba)
while(pom!=x):
    suma+=int(liczba[pom])
    pom+=1
print(suma)
