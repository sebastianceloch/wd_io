import sys
h=int(input("Podaj wysokość wieży: "))
for i in range(1,h,1):
    print("A")
    for z in range(i,0,-1):
        sys.stdout.write('A')
sys.stdout.write('A')
