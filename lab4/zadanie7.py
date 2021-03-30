class Robot:
    def __init__(self,x,y,krok=1):
        self.x = x
        self.y = y
        self.krok = krok
    def idz_w_gore(self,ile_krokow):
        self.ile_k = ile_krokow
        self.y = self.y + self.krok*self.ile_k
        self.x = self.x
        return "ustawiono nowe wartosci wspolrzednych"
    def idz_w_dol(self,ile_krokow):
        self.ile_k = ile_krokow
        self.y = self.y - self.krok*self.ile_k
        self.x = self.x
        return "ustawiono nowe wartosci wspolrzednych"
    def idz_w_lewo(self,ile_krokow):
        self.ile_k = ile_krokow
        self.y = self.y
        self.x = self.x - self.krok*self.ile_k
        return "ustawiono nowe wartosci wspolrzednych"
    def idz_w_prawo(self,ile_krokow):
        self.ile_k = ile_krokow
        self.y = self.y
        self.x = self.x + self.krok*self.ile_k
        return "ustawiono nowe wartosci wspolrzednych"
    def pokaz_gdzie_jestes(self):
        return "znajdujesz sie na wartosciach: ", self.x, self.y
ruch = Robot(0,0,)
print(ruch.idz_w_gore(1))
print(ruch.idz_w_dol(2))
print(ruch.idz_w_lewo(2))
print(ruch.idz_w_prawo(7))
print(ruch.pokaz_gdzie_jestes())
        