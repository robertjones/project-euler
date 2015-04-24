import math
import itertools as it


def primes(lim):
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


Lim = 10**6
Potential_factors = list(primes(math.ceil(Lim**(1/2))))


def isprime(x):
    return not(any(x % factor == 0
                   for factor
                   in it.takewhile(lambda n: n < x, Potential_factors)))


def rotations(num):
    digs = str(num)
    return (int(digs[i:] + digs[0:i]) for i in range(0, len(digs)))


def iscircular(num):
    return all(isprime(rotation) for rotation in rotations(num))


print(sum(1 for prime in primes(Lim) if iscircular(prime)))
