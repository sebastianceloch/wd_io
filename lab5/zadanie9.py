def parzysta(lista):
    for x in range(0,len(lista),2):
        yield lista[x]
lis = parzysta([0,1,2,3,4,5,6,7,8,9,10])
print(next(lis))
print(next(lis))
print(next(lis))
print(next(lis))
print(next(lis))
print(next(lis))