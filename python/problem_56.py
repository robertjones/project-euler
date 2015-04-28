def digits(num):
    return (int(d) for d in str(num))

result = max(sum(digits(a**b)) for a in range(100) for b in range(100))
