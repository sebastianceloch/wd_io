""" Napisz funkcję, która przyjmuje listę wyrazów jako parametr wejściowy. Funkcja losuje jeden z wyrazów jako wyraz do odgadnięcia.
Następnie losowana jest jedna litera tego wyrazu i na wyjściu wyświetlany jest ten niekompletny wyraz, np. wylosowany wyraz to
piłka, wyświetlane jest _ _ ł _ _. Użytkownik wpisuje wyraz o który może chodzić, próbując go odgadnąć, jeżeli zgadł to wyświetlany
jest stosowny komunikat i liczba prób, które były konieczne do odgadnięcia wyrazu. Przy każdej nieudanej próbie losowana jest
kolejna litera tego wyrazu, funkcja kończy działanie po odgadnięciu lub wylosowaniu ostatniej litery wyrazu. """
import random,string
def losy(lista):
    x = list(string.ascii_lowercase)
    random.seed()
    z = random.choice(lista)
    y = random.choice(z)
    x.remove(y)
    for k in range(0,len(x)):
        z.replace(x[k],'_')
    print(z)
    
lista = ["pilka","robak","pies","walec"]
losy(lista)