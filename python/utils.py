"""Utility functions for Project Euler problems."""

import itertools as it
import math


def ispandigital(*nums, pattern=None):
    digits = [int(d) for d in it.chain.from_iterable(str(n) for n in nums)]
    pattern = pattern if pattern else list(range(1, len(digits)+1))
    return sorted(digits) == pattern


def pandigital_gen(hightest_dig, lowest_dig=1):
    return (int("".join(map(str, digs)))
            for digs in it.permutations(range(hightest_dig, lowest_dig-1, -1)))


class Primes:

    def __init__(self, lim=0):
        self.lim = lim
        self.primes = list(self.prime_gen(self.lim))

    def set_primes(self, lim):
        self.primes = list(self.prime_gen(self.lim))

    def prime_gen(self, lim=None):
        D = {}
        q = 2
        while lim is None or q < lim:
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
