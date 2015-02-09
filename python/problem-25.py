def fib():
    a, b = 1, 2
    while True:
        yield a
        a, b = b, a + b
    
print(next(filter(lambda x: x[1] >= 10**(1000-1), enumerate(fib(),2))))