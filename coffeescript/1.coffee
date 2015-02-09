ismultiple = (n, x) -> not (n % x)
sum = (arry) -> arry.reduce (a, b) -> a + b

result = sum(x for x in [1...1000] when ismultiple(x, 3) or ismultiple(x, 5))

console.log(result) # => 233168