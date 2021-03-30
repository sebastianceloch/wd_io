plik = open("dane.txt","w+")
for x in range(1,101,1):
    if(x%4==0):
        plik.writelines(str(x)+" ")
plik.close()