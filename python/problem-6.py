def sum_sq_diff(n):
    nums = range(1,n+1)
    return sum(nums)**2 - functools.reduce(lambda a, e: e**2 + a, nums)

print(sum_sq_diff(100))