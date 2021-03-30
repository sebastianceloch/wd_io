with open("dane.txt","a+") as plik:
    for x in range(1,11,1):
        plik.write(str(x)+" ")
with open("dane.txt","r") as plik:
    for linia in plik:
        print(linia,end="")