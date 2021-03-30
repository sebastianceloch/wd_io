class Ciagi:
    def __init__(self,a1,r,ilosc_wyrazow):
        self.a = a1
        self.r = r
        self.n = ilosc_wyrazow
    def wyswietl_dane(self):
        return (self.a, self.r, self.n)
    def pobierz_elementy(self):
        self.a = int(input("podaj pierwszy wyraz ciagu "))
        self.r = int(input("podaj roznice ciagu "))
        self.n = int(input("podaj ilosc wyrazow ciagu "))
        return "pobrano elementy ciagu"
    def pobierz_parametry(self):
        return (self.a, self.r, self.n)
    def policz_sume(self):
        return (self.a+self.a+(self.n-1)*self.r)/2*self.n
    def policz_elementy(self):
        return self.a+(self.n-1)*self.r
ciag = Ciagi(1,2,2)
print(ciag.wyswietl_dane())
print(ciag.pobierz_elementy())
print(ciag.pobierz_parametry())
print(ciag.policz_sume())
print(ciag.policz_elementy())
