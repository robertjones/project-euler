# To handle long chains can store a list of seen numbers that result in 
# correct path

import itertools as it

def sdchain(start):
    step = start
    while step not in [1, 89]:
        yield step
        step = sum(int(digit)**2 for digit in str(step))
    yield step

def num_89enders(upto):
    ends89 = {89}
    ends1 = {1}
    for n in range(1,upto):
        if n in ends89 or n in ends1:
            continue
        nums = list(sdchain(n))
        if nums[-1] == 89:
            ends89.update(nums)
        elif nums[-1] == 1:
            ends1.update(nums)
    return len(list(filter(lambda x: x<upto, ends89)))

print(num_89enders(10*10**6))
