import itertools as it

tri_nums = (n*(n+1)/2 for n in it.count(1))
pen_nums = (n*(3*n-1)/2 for n in it.count(1))
hex_nums = (n*(2*n-1) for n in it.count(1))

def same():
    p_list, h_list = [], [] 
    for t, p, h in zip(tri_nums, pen_nums, hex_nums):
        p_list.append(p)
        h_list.append(h)
        if t in p_list and t in h_list:
            yield int(t)