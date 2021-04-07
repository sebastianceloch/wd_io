class Kwadrat():
    def __init__(self, x):
        self.x = x
        self.y = x
    def __add__(self, kwadrat):
        return self.x + kwadrat.x


kw = Kwadrat(5)
kw1 = Kwadrat(6)
print(kw+kw1)