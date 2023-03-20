from __future__ import division, print_function
import os
import sys
from io import BytesIO, IOBase


from bisect import bisect_left, bisect_right
from math import gcd, lcm    # Use gcd(*arr) to pass a list
from math import ceil, floor
from datetime import datetime as dt
from itertools import compress

# ======================== Functions declaration Starts ========================

LB = bisect_left
UB = bisect_right
 
def BS(a, x):    # Binary Search
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    else:
        return -1


def isPrime(n):
    if n <= 3: return n > 1
    if n & 1 == 0 or n % 3 == 0: return False
    for i in range(5, ceil(n**0.5)+1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def primesbelow(N=1000000):    # Faster version of Sieve of Erathostenes
    """
    Input N>=3; Returns a list or set of all primes 2 <= p <= N 
    Use this to iterate over prime numbers.
    Don't use this as a substitute for sieve() because
    multiple lookups will be slower than sieve() as one lookup takes logN time.
    """
    N += 1   # To make inclusive of N
    correction = N % 6 > 1
    N = {0:N, 1:N-1, 2:N+4, 3:N+3, 4:N+2, 5:N+1}[N%6]
    sieve_bool = [True] * (N // 3)
    sieve_bool[0] = False
    for i in range(int(N ** .5) // 3 + 1):
        if sieve_bool[i]:
            k = (3 * i + 1) | 1
            sieve_bool[k*k // 3::2*k] = [False] * ((N//6 - (k*k)//6 - 1)//k + 1)
            sieve_bool[(k*k + 4*k - 2*k*(i%2)) // 3::2*k] = [False] * ((N // 6 - (k*k + 4*k - 2*k*(i%2))//6 - 1) // k + 1)
    
    # To return set
    # return {(3 * i + 1) | 1 for i in range(1, N//3 - correction) if sieve_bool[i]}.union({2,3})
    
    # To return list
    return [2, 3] + [(3 * i + 1) | 1 for i in range(1, N//3 - correction) if sieve_bool[i]]

is_prime = []
def sieve(n=1000000):
    global is_prime
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False



# ========================= Functions declaration Ends =========================



def main():
    TestCases = 0
    # TestCases = int(input())

    t1=dt.now()
    sieve()
    # print(is_prime)
    # for _ in range(TestCases):
    #     # n,x,y = [int(i) for i in input().split()]
    #     n = int(input())
    #     arr = [int(i) for i in input().split()]
    t2=dt.now()
    print(t2-t1)





















# =============================== Template Starts ===============================

if sys.version_info[0] < 3:
    class dict(dict):
        def items(self):
            return dict.iteritems(self)
 
        def keys(self):
            return dict.iterkeys(self)
 
        def values(self):
            return dict.itervalues(self)
    from __builtin__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip

# region fastio

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._file = file
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


def print(*args, **kwargs):
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop("sep", " "), kwargs.pop("file", sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        file.write(str(x))
        at_start = False
    file.write(kwargs.pop("end", "\n"))
    if kwargs.pop("flush", False):
        file.flush()


if sys.version_info[0] < 3:
    sys.stdin, sys.stdout = FastIO(sys.stdin), FastIO(sys.stdout)
else:
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)

input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion

if __name__ == "__main__":
    main()