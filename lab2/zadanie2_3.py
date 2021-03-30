import random
matrix = [[random.randrange(1,10,1) for x in range(4)] for y in range(4)]
przekatna = [matrix[i][j] for i in range(0,4,1) for j in range(0,4,1) if i==j]
print(matrix[0])
print(matrix[1])
print(matrix[2])
print(matrix[3])
print('przekatna = ', przekatna)