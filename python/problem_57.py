from sympy import symbols, fraction

def root2(its):
    x = symbols("x")
    expr = 1 + x
    for i in range(1, its+1):
        if i % 50:
            expr = expr.subs(x, 1/(2 + x))
        else:
            expr = expr.subs(x, 1/(2 + x)).factor()
        yield expr.subs(x, 0)


def islonger(pair):
    a, b = pair
    return len(str(a)) > len(str(b))

result = sum(1 for iteration in root2(1000) if islonger(fraction(iteration)))

print(result)
