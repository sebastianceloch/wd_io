def fun(tekst):
    plik = input('wporwadz nazwe pliku ')
    tekst = tekst.lower()
    usun = tekst.replace(',','').replace('.','').split(' ')
    with open(plik,'w') as f:
        f.write('\n'.join([word for word in usun if usun.count(word) == 1]))
tekst = 'Ala ma kota. ala.aa'
fun(tekst)
