# Generate a range of numbers
# Generate a stream of digits from the range
# pick out certain digits
# multiply them

import itertools as it
import functools as fnc
import operator as op

def champ_stream():
	for num in it.count(1):
		for digit in str(num):
			yield int(digit)

def pick_dig(digits, stream):
	return [next(it.islice(stream(), digit-1,digit)) for digit in digits]

dig_list = [1, 10, 100, 10**3, 10**4, 10**5, 10**6]

print(fnc.reduce(op.mul, pick_dig(dig_list, champ_stream)))