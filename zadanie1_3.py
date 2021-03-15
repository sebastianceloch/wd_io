A = [1/x for x in range(1,10)]
print(A)
B = [2**x for x in range(0,10)]
print(B)
C = [i for i in B if i%4==0]
print(C)