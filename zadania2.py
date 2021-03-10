a = input("podaj zdanie \n")
x =a.count(" ")
print(x)
x = int(input("podaj liczbe "))
if x < 0:
    print(x*(-1))
else:
    print(x)
    import sys
print("Podaj jakas liczbe")
s = int(sys.stdin.readline())
print("Podaj druga liczbe")
r = int(sys.stdin.readline())
h = s*r
sys.stdout.write("%s" %h)


a = int(input("pierwsza liczba: "))
b = int(input("druga liczba: "))
c = int(input("trzecia liczba: "))
if a>0 and a<=10:
    print("a zawiera sie w przedziale od 0-10")
else:
    print("a nie zawiera sie w przedziale od 0-10")
if a>b or b>c:
    print("a jest wieksze od b lub b jest wieksze od c")
else:
    print("a nie jest wieksze od b lub b nie jest wieksze od c")
