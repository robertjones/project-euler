from functools import reduce

Factorials = [fact(num) for num in range(10)]

def fact(num):
    return reduce(lambda a, b: a*b, (n for n in range(num, 0, -1)), 1)

def sum_fact_dig(num):
    return sum(Factorials[int(d)] for d in str(num))

def chain(num):
    terms = []
    while num not in terms:
        terms.append(num)
        num = sum_fact_dig(num)
    return terms

result = sum(1 for num in range(1*10**6) if len(chain(num)) == 60)
print(result)
