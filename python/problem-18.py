# See problem-18-2.py for calc method

import itertools as it

triangle_text = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

triangle_text2 = """3
7 4
2 4 6
8 5 9 3"""

def triangle(text):
    return [[int(el) for el in line.split(" ")] for line in text.splitlines()]

def routes(trngl):
    return (it.accumulate(tuple([0]) + tuple(directions))
            for comb in it.combinations_with_replacement([0,1], len(trngl)-1)
            for directions in unique(it.permutations(comb)))

def unique(iterable, key=None):
    seen = set()
    seen_add = seen.add
    for element in it.filterfalse(seen.__contains__, iterable):
        seen_add(element)
        yield element

# def routes2(trngl):
#     values = []
#     for comb in it.combinations_with_replacement([0,1], len(trngl)-1):
#             for directions in set(it.permutations(comb)):
#                 promt
#                 values.append(tuple(0) + tuple(directions))
#     return values

def values(triangle):
    return ([triangle[row][col] for (row, col) in enumerate(route)] 
            for route in routes(triangle))

# print(max(sum(route_vals) for route_vals in values(triangle(triangle_text2))))

# values = []
# count = 0
# for nroute, route in enumerate(routes):
#     position = 0
#     values_route = triangle[0]
#     for step, direction in enumerate(route):
#         position += direction
#         values_route.append((nroute, step+1, position, direction, triangle[step+1][position]))
#         count += 1
#     values.append(values_route)    

# [triange[step][position]]