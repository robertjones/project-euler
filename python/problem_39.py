def side_lengths(perimeter):
    return set(tuple(sorted((a, b, int((a**2 + b**2)**(1 / 2)))))
               for a in range(int(perimeter / 2))
               for b in range(a, int(perimeter / 2))
               if a + b + (a**2 + b**2)**(1 / 2) == perimeter)


if __name__ == '__main__':

    result = max((len(side_lengths(p)), p) for p in range(1000))

    print(result)
