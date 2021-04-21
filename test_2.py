def zlicz(a):
    d = 0
    m = 0
    for i in range (len(a)):
        if a[i].isupper():
            d=d+1
        if a[i].islower():
            m=m+1
    return "mała = ",m," duża= ",d
a = input("wpisz tekst ")
print(zlicz(a))