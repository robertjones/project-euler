"""Calculate a solution to Project Euler problem 49."""

from utils import Primes
import itertools as it
from collections import defaultdict

P = Primes(10000)


def prime_perms(num):
    """Return all permutations of num that are prime."""
    return set(perm
               for perm in (int("".join(tup))
                            for tup in it.permutations(str(num)))
               if P.isprime(perm))


def arith_seq(nums):
    """Return an array of three number arithmetic sequences from nums."""
    diffs = defaultdict(list)

    for pair in it.combinations(nums, 2):
        diffs[pair[1] - pair[0]].append(pair)

    poss_chains = {diff: set(point for pair in pairs for point in pair)
                   for diff, pairs in diffs.items() if len(pairs) >= 2}

    return [tuple(point + diff*n for n in range(3))
            for diff, points in poss_chains.items()
            for point in points
            if all(point + diff*n in points for n in range(3))]


def flatten(iterable):
    """Return a flattened generator from an iterable."""
    return (item for it in iterable for item in it)


seqs = flatten(arith_seq(prime_perms(prime))
               for prime in P.primes if prime >= 1000)

result = set(seq for seq in seqs if seq and all(num > 999 for num in seq))

print(result)
