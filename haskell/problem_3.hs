primes = 2 : [x | x <- [3,5..], all ((> 0).(rem x)) $ takeWhile ((<=x).(^2)) primes]
primeFactors x = [p | p <- takeWhile (<= div x 2 + 1) primes, rem x p == 0]
main = print $ last $ primeFactors 600851475143
