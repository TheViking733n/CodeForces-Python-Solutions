from math import gcd
from timeit import repeat
from statistics import mean


"""
Conclusion:

math.gcd is more than 3 times faster than iterative while loop version of gcd

"""



def gcd1(x, y):
    """ greatest common divisor of x and y """
    while y:
        x, y = y, x % y
    return x

def func():
    for i in range(1000):
        ans = gcd(3442, 35568)
    return
    


timings = repeat(func, number=1000)

mn = min(timings)
# avg = mean(timings)
# mx = max(timings)

print("Minimum execution time:", mn)
# print("Average execution time:", avg)
# print("Maximum execution time:", mx)