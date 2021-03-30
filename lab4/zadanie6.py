class Slowa:
    def __init__(self,slowo1,slowo2):
        self.s1 = slowo1
        self.s2 = slowo2
    def sprawdz_czy_palindrom(self):
        return self.s1 == self.s1[::-1], self.s2 == self.s2[::-1]
    def sprawdz_czy_metagramy(self):
        p=0
        for i in range(0,len(self.s1),1):
            if(self.s1[i]!=self.s2[i]):
                p+=1
        if(p==1):
            return "wyrazy to metagramy"
        elif(p!=1):
            return "wyrazy to nie metagramy"
    def sprawdz_czy_anagramy(self):
        if(sorted(self.s1) == sorted(self.s2)):
            return "wyrazy to anagramy"
        else:
            return "wyrazy to nie anagramy"
    def wyswietl_wyrazy(self):
        return self.s1, self.s2
    def __del__(self):
        print ("finalizer")


slownik = Slowa("listen","silent")
print(slownik.sprawdz_czy_palindrom())
print(slownik.sprawdz_czy_metagramy())
print(slownik.sprawdz_czy_anagramy())
print(slownik.wyswietl_wyrazy())
#dodalem tutaj zadanie 8 czyli finalizer