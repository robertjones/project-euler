import math

def tri_nums():
    i, num = 1, 1
    while True:
        yield num
        i += 1
        num += i

def divisors(num):
    divisors = []
    for i in range(1, int(math.sqrt(num) + 1)):
        if num % i is 0:
            divisors.append(i)
            if i is not num/i:
                divisors.append(int(num/i))
    return divisors

print(next(filter(lambda x: len(divisors(x)) > 500, tri_nums())))