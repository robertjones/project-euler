from utils import Primes

def diagonals():
    n, spacing = 1, 2
    yield n
    while True:
        for _ in range(4):
            n += spacing
            yield n
        spacing += 2

def diagonal_layers(seq):
    yield [next(seq)]
    while True:
        yield [next(seq), next(seq), next(seq), next(seq)]

def layer_target(seq, target_ratio):
    primes, total = 0, 0
    nums = next(seq)
    primes += sum(1 for num in nums if P.isprime(num))
    total += len(nums)
    while True:
        nums = next(seq)
        primes += sum(1 for num in nums if P.isprime(num))
        total += len(nums)
        if primes/total < target_ratio:
            break
    side_length = nums[1] - nums[0] + 1
    return side_length

P = Primes(1000000)

result = layer_target(diagonal_layers(diagonals()), 10/100)
print(result)
