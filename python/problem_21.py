import itertools as it

def unique(a, b):
    return (a,) if a == b else (a, b)

def divisors(n):
    return it.chain(*(unique(i,(int(n/i) if i != 1 else 1)) 
                      for i in range(1,int(n**0.5)+1) if n % i == 0))

def amicable():
    return (n for n in it.count(1) 
            if sum(divisors(sum(divisors(n)))) == n and sum(divisors(n)) != n)

print(sum(it.takewhile(lambda x: x < 10000, amicable())))