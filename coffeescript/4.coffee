ld = require('lodash')

isPal = (num) -> 
  arr1 = num.toString().split("")
  arr2 = num.toString().split("").reverse()
  ld.isEqual(arr1, arr2)

result = ld(i*j for j in [100..999] for i in [100..999])
         .flatten().filter(isPal).max()

console.log(result) # => 906609