def calc(triangle):
    values = []
    for r, row in enumerate(triangle):
        if r == 0:
            el = row[0]
            row_values = [(el, (el,), (0,))]
        else:
            row_values = []
            for c, el in enumerate(row):
                max_prev = max([(values[r-1][c-1] if c >= 0 else (0,)), 
                                (values[r-1][c] if c <= len(values[r-1])-1 
                                 else (0,))])
                r_sum, r_vals, r_cols = max_prev
                row_values.append((r_sum + el, r_vals + (el,), r_cols + (c,)))
        values.append(row_values)
    return max(values[-1])

def calc2(triangle):
    values = []
    for r, row in enumerate(triangle):
        if r == 0:
            row_values = row[0]
        else:
            row_values = []
            for c, el in enumerate(row):
                max_prev = max([(values[r-1][c-1] if c >= 0 else 0), 
                                (values[r-1][c] if c <= len(values[r-1])-1 
                                 else 0)])
                row_values.append(max_prev + el)
        values.append(row_values)
    return max(values[-1])