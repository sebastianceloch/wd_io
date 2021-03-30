class NaZakupy:
    def __init__(self,nazwa_produktu,ilosc,jednostka_miary,cena_jed):
        self.x = nazwa_produktu
        self.y = ilosc
        self.z = jednostka_miary
        self.c = cena_jed
    def wyswietl_produkt(self):
        return(self.x,self.y,self.z,self.c)
    def ile_produktu(self):
        return(self.y, self.z)
    def ile_kosztuje(self):
        return self.y*self.c
zakup = NaZakupy("ser",2,"kg",4)
print(zakup.wyswietl_produkt())
print(zakup.ile_produktu())
print(zakup.ile_kosztuje())


