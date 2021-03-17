def dzien_tyg(a):
    if a == 1:
        return "poniedzialek"
    elif a == 2:
        return "wtorek"
    elif a == 3:
        return "sroda"
    elif a == 4:
        return "czwartek"
    elif a == 5:
        return "piatek"
    elif a == 6:
        return "sobota"
    elif a == 7:
        return "niedziela"
    else:
        return "nie ma takiego dnia tygodnia"
def skroc_dzien(a):
    if a == "pn":
        return "poniedziałek"
    elif a == "wt":
        return "wtorek"
    elif a == "sr":
        return "sroda"
    elif a == "czw":
        return "czwartek"
    elif a == "pt":
        return "piatek"
    elif a == "sb":
        return "sobota"
    elif a == "ndz":
        return "niedziela"
    else:
        return "zly skrot/nie ma takiego dnia tygodnia"
print(dzien_tyg(3))
print(skroc_dzien("wt")) 
