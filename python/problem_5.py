import functools
import operator

def is_multiple(x, nums):
    return all(x % num == 0 for num in nums)

def factors(x):
    return [i for i in range(x,0,-1) if x % i == 0]

def is_prime(x):
    return set(factors(x)) == set([x, 1])

def primes(nums):
    return [num for num in nums if is_prime(num)]

def smallest_multiple(nums):
    primes_product = functools.reduce(operator.mul,primes(nums))
    i = primes_product
    while not is_multiple(i, nums): i += primes_product
    return i

smallest_multiple(range(1,21,1))