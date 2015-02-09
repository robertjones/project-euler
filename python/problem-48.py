# Problem 48 - Self powers

import itertools as it

def self_powers():
    return (n**n for n in it.count(1))

print(str(sum(it.islice(self_powers(),1000)))[-10:])
