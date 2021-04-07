class Material:
    def __init__(self,rodzaj,dlugosc,szerokosc):
        self.r = rodzaj
        self.d = dlugosc
        self.sz = szerokosc
    def wyswietl_nazwe(self):
        return (self.r)
class Ubrania(Material):
    def __init__(self,rozmiar,kolor,dla_kogo):
        self.r = rozmiar
        self.k = kolor
        self.dla = dla_kogo
    def wyswietl_dane(self):
        return (self.r, self.k, self.dla)
class Sweter(Ubrania):
    def __init__(self,rodzaj_swetra):
        self.r = rodzaj_swetra
    def wyswietl_dane(self):
        return self.r
swtr = Sweter("w paski")
mat = Material("blabla",4,4)
ub = Ubrania(4,"czarny","kobiety")
print(mat.wyswietl_nazwe())
print(ub.wyswietl_dane())
print(swtr.wyswietl_dane())