def bouncy(num):
    digs = list(int(dig) for dig in str(num))
    return not(all(a >= b for a, b in pairs(digs))
               or all(a <= b for a, b in pairs(digs)))

def pairs(items):
    return ((items[idx], items[idx+1]) for idx in range(len(items)-1))

num_bouncy = 0
num = 0

while True:
    num += 1
    num_bouncy += 1 if bouncy(num) else 0
    if num_bouncy / num == 0.99:
        break

print(num)
