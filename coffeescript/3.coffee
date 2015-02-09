num = 600851475143

primeGen = ->
  cache = []
  i = 2
  loop
    if cache.every((p) -> not (i%p==0))
      yield i
      cache.push(i)
    i++

primeFactors = (n) ->
  results = []
  primes = primeGen()
  p = primes.next().value
  while p <= n**(1/2)
    if n%p==0
      results.push(p)
    p = primes.next().value
  return results

max = (arr) -> arr.reduce (a,b) -> Math.max(a,b)

result = max(primeFactors(num))
console.log(result) # => 6857