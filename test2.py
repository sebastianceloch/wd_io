class Material:
    def __init__(self,rodzaj,dlugosc,szerokosc):
        self.rodzaj = rodzaj
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc
    def wyswietl_nazwe(self):
        return self.rodzaj
class Ubrania(Material):
    def __init__(self,rozmiar,kolor,dla_kogo,rodzaj,dlugosc,szerokosc):
        Material.__init__(self,rodzaj,dlugosc,szerokosc)
        self.rozmiar = rozmiar
        self.kolor = kolor
        self.dla_kogo = dla_kogo
    def wyswietl_dane(self):
        return self.__dict__
ciuch = Material("rodzaj",4,3)
adrian = Ubrania("L","czerwony","kobiety","rodzaj",4,3)
print (ciuch.wyswietl_nazwe())
print (adrian.wyswietl_dane())
