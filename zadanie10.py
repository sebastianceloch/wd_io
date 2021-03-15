import sys
h=int(input("Podaj wysokość wieży od 1 do 10: "))
if h > 10:
    print("podales za duza wysokosc")
else:
    for i in range(1,h,1):
        print("A")
        for z in range(i,0,-1):
            sys.stdout.write('A')
sys.stdout.write('A')


