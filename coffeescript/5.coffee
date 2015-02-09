ld = require('lodash')
upper = 20

divs = ld.reduce([upper...1], 
       ((acc, n) -> if ld.every(acc, ((m) -> m%n!=0)) \ 
                    then acc.concat(n) else acc), [])

smallestEvenlyDivisable = ->
  i = upper
  loop
    return i if ld.every(divs, ((div) -> i%div==0))
    i++

console.log(smallestEvenlyDivisable()) # => 232792560