def is_palindromic(num):
    return str(num) == str(num)[::-1]

def palindromic_products():
    results = []
    for i in range(999,0,-1):
        for j in range(999,0,-1):
            if is_palindromic(i*j): results.append(i*j)
    return results

max(palindromic_products()) # => 906609