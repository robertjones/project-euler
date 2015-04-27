import csv
import math

filename = 'p099_base_exp.txt'
file = open(filename)
pairs = csv.reader(file)

values = (int(line[1])*math.log(int(line[0])) for line in pairs)
max_line = max((value, i)for i, value in enumerate(values, 1))

print(max_line)