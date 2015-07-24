pyramidal = tuple(sum(digs) for digs in it.product([1,2,3,4], repeat=9))

cubic = tuple(sum(digs) for digs in it.product([1,2,3,4,5,6], repeat=6))

p_hist = [0]*(4*9+1)
for num in pyramidal:
    p_hist[num] += 1

c_hist = [0]*(6*6+1)
for num in cubic:
    c_hist[num] += 1

p_wins = sum(c_hist[i] * p_hist[j]
             for i in range(len(c_hist))
             for j in range(len(p_hist))
             if j > i)

combos = sum(p_hist) * sum(c_hist)

print(p_wins / combos)
