class Kwadrat():
    def __init__(self, x):
        self.x = x
        self.y = x
    def __ge__(self,kwadrat):
        return self.x >= kwadrat.x
    def __gt__(self,kwadrat):
        return self.x > kwadrat.x
    def __le__(self,kwadrat):
        return self.x <= kwadrat.x
    def __lt__(self,kwadrat):
        return self.x <=kwadrat.x

kw = Kwadrat(5)
kw1 = Kwadrat(7)
kw2 = Kwadrat(2)
kw3 = Kwadrat(2)
print(kw>=kw3)
print(kw>kw1)
print(kw2<=kw3)
print(kw<kw1)