from utils import pandigital_gen


def digs(num, start_digit, end_digit):
    return int(str(num)[start_digit-1:end_digit])


def is_sub_string_div(num):
    return all(digs(num, n, n+2) % p == 0
               for n, p in zip(range(8, 1, -1), [17, 13, 11, 7, 5, 3, 2]))


if __name__ == '__main__':
    result = sum(num
                 for num in pandigital_gen(9, lowest_dig=0)
                 if is_sub_string_div(num))
    print(result)
