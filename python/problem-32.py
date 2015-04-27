import itertools as it


def ispandigital(*nums, pattern=None):
    digits = [int(d) for d in it.chain.from_iterable(str(n) for n in nums)]
    pattern = pattern if pattern else list(range(1, len(digits)+1))
    return sorted(digits) == pattern


def pairs():
    return it.chain.from_iterable(
        ((int(a), int(b+c+d+e)), (int(a+b+c), int(d+e)))
        for a, b, c, d, e in it.permutations("123456789", r=5)
    )


pandigial_products = set(
    first*second
    for first, second in pairs()
    if ispandigital(first, second, first*second, pattern=list(range(1, 10)))
)

print(sum(pandigial_products))
