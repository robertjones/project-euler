# Work in progress

from fractions import Fraction as F

def term(iterations):
    return Fraction(2 + 1/(2 if iterations <= 0 else term(iterations-1)))

def root2v2(iterations):
    i = iterations
    return "F(-1) +" + "F(2) + F(1/(" * i + "2" + "))" * i

def root2(iterations):
    return term(iterations) - 1

def longer_numerator(frac):
    return len(str(frac.numerator)) - len(str(frac.denominator)) > 0

result = sum(1 for its in range(1, 100) if longer_numerator(eval(root2v2(its))))

print(result)