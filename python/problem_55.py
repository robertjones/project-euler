def addreverse(num, max_iter):
    for _ in range(max_iter):
        result = num + int(str(num)[::-1])
        yield result
        num = result

def palindromic(num):
    return num == int(str(num)[::-1])

def lychrel(num):
    return not any(palindromic(result) for result in addreverse(num, 50))

num_lychrel_nums = sum(1 for n in range(10000) if lychrel(n))

print(num_lychrel_nums)