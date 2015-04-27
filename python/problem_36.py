def is_dec_bin_pal(num):
    dec = str(num)
    binary = bin(num)[2:]
    return dec == dec[::-1] and binary == binary[::-1]

print(sum(num for num in range(1,10**6) if is_dec_bin_pal(num))0)