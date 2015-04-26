import itertools as it
import math


class Primes:

    def __init__(self, lim):
        self.lim = lim
        self.primes = list(self.prime_gen(self.lim))

    def set_primes(self, lim):
        self.primes = list(self.prime_gen(self.lim))

    def prime_gen(self, lim):
        D = {}
        q = 2
        while q < lim:
            if q not in D:
                yield q
                D[q * q] = [q]
            else:
                for p in D[q]:
                    D.setdefault(p + q, []).append(p)
                del D[q]
            q += 1

    def isprime(self, x):
        if x <= 1:
            return False
        if x == 2:
            return True
        top_check = math.ceil(x ** (1/2))
        if top_check > self.lim - 1:
            raise ValueError('Insufficient primes generated')
        return not(any(x % factor == 0
                       for factor
                       in it.takewhile(lambda n: n <= top_check, self.primes)))


def count(iterable):
    return sum(1 for iteration in iterable)


Lim = 1000
isprime = Primes(Lim+1).isprime

result = max(
    (count(it.takewhile(isprime, (n**2+a*n+b for n in it.count()))), a*b, a, b)
    for a in range(-Lim+1, Lim)
    for b in range(-Lim+1, Lim)
)

print(result)
