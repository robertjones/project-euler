from utils import Primes
import itertools as it

Lim = 10**6
p = Primes(Lim)


def max_prime_sum_primes(start):
    return max(
        acc
        for acc in enumerate(it.takewhile(lambda x: x < Lim,
                                          it.accumulate(p.primes[start:])), 1)
        if p.isprime(acc[1])
    )


if __name__ == '__main__':

    max_so_far = (1, 2)
    for start in range(len(p.primes)):
        if len(p.primes) - start < max_so_far[0]:
            break
        else:
            max_so_far = max(max_so_far, max_prime_sum_primes(start))

    print(max_so_far)
