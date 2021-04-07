import itertools
zbior = [1,2,3,4,2,3,6,8,7,6]
x = list(itertools.combinations(zbior,3))
unq = set(x)
result = list(unq)
print(unq)