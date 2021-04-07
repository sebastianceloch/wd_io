def miesiace():
    miesiac = ['Styczen','Luty','Marzec','Kwiecien','Maj','Czerwiec','Lipiec','Sierpien','Wrzesien','Pazdziernik','Listopad','Grudzien']
    for x in range(0,12,1):
        yield miesiac[x]
mies = miesiace()
for i in range(0,12,1):
    print(next(mies))