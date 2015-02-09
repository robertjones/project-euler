# Works but is slow

import itertools as it

def unique(a, b):
    return (a,) if a == b else (a, b)

def divisors(n):
    return it.chain(*(unique(i,(int(n/i) if i != 1 else 1)) 
                      for i in range(1,int(n**0.5)+1) if n % i == 0))

def abundants_up_to(x):
    return list(n for n in range(12,x+1) if sum(divisors(n)) > n)

sum_of_abundants_list = set(a+b for a in abundants_up_to(28123) 
                            for b in abundants_up_to(28123-a)
                            if a+b <= 28123)

non_abundants = [n for n in range(28123+1) if n not in sum_of_abundants_list]

print(sum(non_abundants))