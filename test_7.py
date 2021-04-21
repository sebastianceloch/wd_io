import random
def los(ile,przedzial):
    random.seed()
    num = [random.randint(*przedzial) for i in range(ile)]
    print(num)
    print(sum(num), sum(num)/len(num))
los(5,(1,100))