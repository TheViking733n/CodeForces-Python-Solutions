def find_smallest_n(m):
    r = 2
    s = 0
    
    while 1:
        prod = r*r*r
        val = m//prod
        if val==0:
            break
        s += val
        r += 1
    return s


print(find_smallest_n(139840))
