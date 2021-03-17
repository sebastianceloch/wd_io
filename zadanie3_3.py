produkty = {"mleko": "litr", "ser": "kg", "szynka": "kg", "jajka": "sztuki"}
odwrocone = {value: key for key, value in produkty.items()}
print(produkty)
print(odwrocone)