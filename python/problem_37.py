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
        if x == 1:
            return False
        if x == 2:
            return True
        top_check = math.ceil(x ** (1/2))
        if top_check > self.lim - 1:
            raise ValueError('Insufficient primes generated')
        return not(any(x % factor == 0
                       for factor
                       in it.takewhile(lambda n: n <= top_check, self.primes)))


def truncate(num):
    trunc = str(num)
    for i in range(len(trunc)-1, 0, -1):
        yield int(trunc[i:])
        yield int(trunc[:-i])
    yield num


def istruncatable(prime, prime_check):
    return all(prime_check(trunc) for trunc in truncate(prime)) and prime >= 10


p = Primes(10**6)
trunc_primes = (prime for prime in p.primes if istruncatable(prime, p.isprime))
tp_list = list(it.islice(trunc_primes, 11))

print(tp_list)
print(sum(tp_list))
