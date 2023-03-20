from timeit import repeat
from statistics import mean
from math import ceil

def isPrime1():   # Execution time 47ms
    n=1000000007
    if n <= 3:
        return n > 1
    if n & 1 == 0 or n % 3 == 0:
        return False
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def isPrime2():   # Execution time 31ms
    n=1000000007
    if n <= 3: return n > 1
    if n & 1 == 0 or n % 3 == 0: return False
    for i in range(5, ceil(n**0.5)+1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def isPrime3():   # Execution time 90ms
    n=1000000007
    if n & 1 == 0:
        return True
    d = 3
    while d * d <= n:
        if n % d == 0:
            return True
        d = d + 2
    return False

timings = repeat(isPrime2, number=100)

mn = min(timings)


print("Minimum execution time:", mn)
