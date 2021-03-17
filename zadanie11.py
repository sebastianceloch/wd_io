import sys
h=int(input("Podaj wysokosc diamentu: "))
if h<3 or h>10:
    print("za malo lub za duza wysokosc")
else:
    s=h/2
    x=h
    r=1
    j=3
    while(x>s):
        print(" "*int(j)+ "o"*int(r))
        r+=2
        j-=1
        x-=1
    while(x>=0):
        print(" "*int(j)+"o"*int(r))
        r-=2
        j+=1
        x-=1


