_ = require 'lodash'
bigInt = require 'big-integer'

sum = (arry) ->
  _.reduce arry, (a, b) -> bigInt(a).plus(b)

sum_digs = (n) ->
  sum(parseInt(digit) for digit in n.toString())

console.log sum_digs(bigInt(2).pow(1000)).toJSNumber() # => 1366