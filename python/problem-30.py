def is_sum_pow(num, power):
    return num == sum(int(d)**power for d in str(num))

fives = (x for x in range(2,300*10**3) if is_sum_pow(x,5))

print(sum(fives))