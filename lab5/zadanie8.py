class Samogloski:
    def __init__(self, napis):
        if isinstance(napis, str):
            self.napis = napis
            self.index = 0
            self.lista = ['a','ą','e','ę','i','o','ó','u','y','A','Ą','E','Ę','I','O','Ó','U','Y']

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.napis):
            raise StopIteration
        while self.index < len(self.napis):
            if self.napis[self.index] in self.lista:
                self.index+=1
                return self.napis[self.index-1]
            self.index+=1
gen = Samogloski("woyioraae")
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))