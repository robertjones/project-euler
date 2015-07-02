import itertools as it

def primes():
    for n in it.count(2):
        if all(n % m != 0 for m in range(2, int(n**0.5)+1)):
            yield n

def isprime(num):
    return all(num % prime != 0 
               for prime in it.takewhile(lambda x: x <= num**0.5, primes()))

def isgoldback(num):
    return any(((num-prime)/2)**0.5 % 1 == 0
               for prime in it.takewhile(lambda x: x <= num-2, primes()))

conjecture_breakers = (num 
                       for num in it.count(1,2)
                       if not isprime(num) and not isgoldback(num))

first_breaker = next(conjecture_breakers)

print(first_breaker)