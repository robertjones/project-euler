import itertools as it

m_prm = "".join(next(it.islice(it.permutations("0123456789"), 10**6-1, 10**6)))

print(m_prm)
