nthPrime = (n) ->
  cache = []
  x = 2
  i = 0
  loop
    if cache.every((p) -> not (x%p==0))
      cache.push(x)
      i++
    return x if i == n 
    x++

console.log(nthPrime(10001)) # => 104743