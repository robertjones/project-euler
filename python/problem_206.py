def check(num):
    return all(str(num)[i] == "1_2_3_4_5_6_7_8_9_0"[i]
               for i in range(0, 19, 2))

low = int(1020304050607080900**0.5)
high = int(1929394959697989990**0.5)

results = (num for num in range(low, high, 10) if check(num**2))

print(next(results))
