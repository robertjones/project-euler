primes = ->
  cache = []
  i = 2
  loop
    if cache.every((p) -> not (i%p==0))
      yield i
      cache.push(i)
    i++

sumSeries = (gen, threshold) ->
  series = gen()
  sum = 0
  current = 0
  while current < threshold
    sum += current
    current = series.next().value
  return sum

console.log(sumSeries(primes, 2*10**6)) # => 142913828922