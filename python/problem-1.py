def is_multiple(x):
    """Tests if the number is a multiple of 3 or 5"""
    return (not x % 3) or (not x % 5)

sum(x for x in range(1,1000) if is_multiple(x)) # => 233168