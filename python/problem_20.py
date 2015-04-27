import operator as op
import functools as fnc

def fact(n):
    """Return n factorial"""
    return fnc.reduce(op.mul, range(n,1,-1))

def sum_dig(num):
    """Return the sum of the digits in num"""
    return sum(int(d) for d in str(num))

print(sum_dig(fact(100))) #>648 - correct answer