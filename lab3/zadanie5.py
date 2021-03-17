def rowno_czy_prost(a1,b1,a2,b2):
    if(a1==a2):
        return "proste sa rownolegle"
    elif(a1*a2==-1):
        return "proste sa prostopadle"
    else:
        return "proste nie sa prostopadle i rownolegle"
print(rowno_czy_prost(3,2,-(1/3),4))

