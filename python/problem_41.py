from utils import ispandigital, pandigital_gen, Primes
import itertools as it

isprime = Primes(10**5).isprime
max_pan_prime = next(pan_dig
                     for n in range(9, 0, -1)
                     for pan_dig in pandigital_gen(n) if isprime(pan_dig)
                    )

if __name__ == '__main__':
    print(max_pan_prime)
