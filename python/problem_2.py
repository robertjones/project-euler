def fib():
    a, b = 1, 2
    while a < 4000000:
        yield a
        a, b = b, a + b
    
sum(x for x in fib() if x % 2 == 0) # => 4613732