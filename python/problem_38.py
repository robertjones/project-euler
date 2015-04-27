import itertools as it


def ispandigital(*nums, pattern=None):
    """Check if the numbers are collectively pandigital or are pattern."""
    digits = [int(d) for d in it.chain.from_iterable(str(n) for n in nums)]
    pattern = pattern if pattern else list(range(1, len(digits)+1))
    return sorted(digits) == pattern


def advance_iterator(iterator, n):
    """Advance the iterator n-steps ahead."""
    next(it.islice(iterator, n, n), None)


def concat_prod(n, length, min_upto):
    """Return the concatonated product of specified length or False."""
    acc = it.accumulate((str(n*x) for x in range(1, length+1)),
                        lambda x, y: x+y)
    nums = it.takewhile(lambda x: len(x) <= length, acc)
    advance_iterator(nums, min_upto-1)
    return (next((int(num) for num in nums if len(num) == length), False), n)


if __name__ == '__main__':
    result = max((num, n)
                 for num, n in (concat_prod(n, 9, 2) for n in range(1, 10**5))
                 if num and ispandigital(num))
    print(result)
