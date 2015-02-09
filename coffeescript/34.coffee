_ = require 'lodash'

fact = (n) ->
  return 1 if n == 0
  _.reduce [n..1], (a, b) -> a * b

digFact = (num) -> 
  _(fact(parseInt(dig)) for dig in num.toString()).reduce (a,b) -> a + b

ans = _([3..digFact(10**7-1)])
  .filter((num) -> num == digFact(num))
  .reduce((a, b) -> a + b)

console.log(ans) # => 40730