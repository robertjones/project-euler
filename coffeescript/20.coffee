_ = require 'lodash'
bigInt = require 'big-integer'

fact = (n) ->
  return 1 if n == 0
  _.reduce [n..1], (a, b) -> bigInt(a).multiply(b)

sum = (arry) ->
  _.reduce arry, (a, b) -> bigInt(a).plus(b)

sum_digs = (n) ->
  sum(parseInt(digit) for digit in n.toString())

console.log sum_digs(fact(100)).toJSNumber() # => 648