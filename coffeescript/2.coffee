fib = ->
  [a, b] = [1, 2]
  results = []
  while a < 4 * 10**6
    results.push(a)
    [a, b] = [b, a + b]
  return results

iseven = (x) -> not (x % 2)
sum = (arry) -> arry.reduce (a, b) -> a + b

result = sum(x for x in fib() when iseven(x))
console.log(result) # => 4613732