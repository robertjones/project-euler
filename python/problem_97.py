def pow_end_only(a, b, digits):
    result = 1
    for _ in range(b):
        result = int(str(result*a)[-digits:])
    return result


print(str(28433 * pow_end_only(2,7830457, 10) + 1)[-10:])
