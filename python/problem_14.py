def collatz(n):
    while n != 1:
        yield n
        if n % 2:
            m = 3*n + 1
        else:
            m = n/2
        n = m
    else:
        yield 1

def largest_collatz(n):
    return max((sum(1 for n in collatz(x)),x) for x in range(n,1,-1))

largest_collatz(1000000) # => (525, 837799)