
def ways(num):
    if num < 2:
        return num
    return [(ways(num-k), ways(k)) for k in range(1,int(num/2)+1)]
