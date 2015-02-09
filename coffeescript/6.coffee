# (a + b)^2 - (a^2 + b^2) = 2ab
# (a + b + c)^2 - (a^2 + b^2 + c^2) = 2ab + 2ac + 2bc

ld = require('lodash')

sum = (nums) ->
  ld.reduce(nums, ((a,b) -> a + b) )

sumSquares = (nums) ->
  sum(num**2 for num in nums)

squareSum = (nums) ->
  sum(nums)**2

result = squareSum([1..100]) - sumSquares([1..100])

console.log(result) # => 25164150