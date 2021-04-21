""" Napisz funkcję, która z klawiatury przyjmuje tekst postaci „Imię Nazwisko” a następnie na wyjściu wyświetla, np. Marek Kowalski ->
MK . Funkcja powinna sprawdzać i ewentualnie zamieniać pierwsze małe litery imienia i nazwiska na wielkie, czyli jeżeli
wprowadzone zostanie marek kowalski to na wyjściu i tak będzie Marek Kowalski -> MK. Funkcja kończy działanie po wpisaniu słowa
koniec. """
def skrot(imie):
    if (imie=='koniec'):
        return "nic"
    else:
        nazwisko = imie.split()
        imie = nazwisko[0]
        naz = nazwisko[1]
        return imie.capitalize(),naz.capitalize(), imie[0].capitalize()+naz[0].capitalize()
imie = input("Podaj imie ")
print(skrot(imie))