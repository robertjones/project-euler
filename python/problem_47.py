import itertools as it
from utils import Primes
from winsound import MessageBeep


p = Primes()
primes = p.prime_gen


def collect(seed, iterable):
    return it.accumulate(it.chain([seed], iterable),
                         lambda collection, el: collection[1:] + [el])


def uniq_factors(num, num_primes):
    # Could reduce search space by taking factors already found into account
    prime_max = num/(1 if num_primes == 1 else
                     2 if num_primes == 2 else
                     2*3 if num_primes == 3 else
                     2*3*5)
    return tuple(prime
                 for prime in it.takewhile(lambda x: x <= prime_max, primes())
                 if num % prime == 0)


def consec_prime_factors(factors, consec):
    return (tuple(el[0] for el in collection)
            for collection in collect(
                [(0, False)]*consec,
                ((i, len(uniq_factors(i, factors)) == factors)
                 for i in it.count(2)))
            if all(el[1] for el in collection))


a = consec_prime_factors(4, 4)
print(next(a))
MessageBeep()
