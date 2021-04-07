def reverse(data):
    if(len(data)%2==0):
        for index in range(1,len(data), 2):
            yield data[index]
    else:
        for index in range(1,len(data), 2):
            yield data[index]


gen = reverse("Feliksasdaar")
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))