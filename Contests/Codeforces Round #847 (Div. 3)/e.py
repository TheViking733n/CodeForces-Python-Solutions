# for a in range(1, 20):
#     for b in range(a, 20):
#         if not a+b == (a^b) + ((a&b)<<1):
#             print(a, b)

x = 562

def check(x):
    for a in range(1, x+1):
        b = 2 * x - a
        if a & b:
            continue
        if (a + b) // 2 == a ^ b:
            return a, b
    
    return None


# print(check(x))

for x in range(2, 10001, 2):
    a1, b1 = x//2, 3*(x//2)
    f = ((a1 + b1) // 2 == a1 ^ b1)
    y = check(x)
    if not f and y:
        print(x, y)




            