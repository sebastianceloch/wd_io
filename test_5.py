def znaki(tekst):
    slownik = {i:tekst.count(i) for i in list(tekst)}
    return slownik
print(znaki("retutu"))