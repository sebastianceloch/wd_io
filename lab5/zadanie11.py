def fib(n):
    a=0
    b=1
    for _ in range(n):
        yield a
        temp = a+b
        a = b
        b = temp
print(list(fib(5)))