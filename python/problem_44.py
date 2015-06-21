import itertools as it
import winsound

def pent(n):
    return int(n*(3*n-1)/2)

pent_gen = (pent(n) for n in it.count(1))
pent_nums = [next(pent_gen)]

def is_pent(num):
    while num > pent_nums[-1]:
        pent_nums.append(next(pent_gen))
    return num in pent_nums

def main():
    pairs = ((pent(j), pent(k), pent(j) - pent(k))
             for j in range(1, 1000) for k in range(j, 1, -1)
             if is_pent(pent(j) - pent(k)) and is_pent(pent(j) + pent(k)))

    first_pair = next(pairs)

    print(first_pair)
    winsound.Beep(500, 1000)
