from __future__ import division, print_function
import os,sys
from io import BytesIO, IOBase

if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip




from math import ceil, floor, factorial
# from math import log,sqrt,cos,tan,sin,radians
from bisect import bisect_left, bisect_right
from collections import defaultdict
# from collections import deque, Counter, OrderedDict
# from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace
# from bisect import bisect,bisect_left,bisect_right,insort,insort_left,insort_right
# from decimal import *

# from itertools import permutations

# ======================== Functions declaration Starts ========================


abc='abcdefghijklmnopqrstuvwxyz'
abd={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}


M=1000000007
# M=998244353
INF = float("inf")
PI = 3.141592653589793

def copy2d(lst): return [x[:] for x in lst]   #Copy 2D list... Avoid Using Deepcopy
def isPowerOfTwo(x): return (x and (not(x & (x - 1))) )

LB = bisect_left   # Lower bound
UB = bisect_right  # Upper bound
 
def BS(a, x):      # Binary Search
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    else:
        return -1

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return (x*y)//gcd(x,y)

# import threading
# def dmain():
#     sys.setrecursionlimit(1000000)
#     threading.stack_size(1024000)
#     thread = threading.Thread(target=main)
#     thread.start()
from collections import Counter


def gcd(x, y):
    """greatest common divisor of x and y"""
    while y:
        x, y = y, x % y
    return x


def memodict(f):
    """memoization decorator for a function taking a single argument"""
    class memodict(dict):
        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret

    return memodict().__getitem__


def pollard_rho(n):
    """returns a random factor of n"""
    if n & 1 == 0:
        return 2
    if n % 3 == 0:
        return 3

    s = ((n - 1) & (1 - n)).bit_length() - 1
    d = n >> s
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        p = pow(a, d, n)
        if p == 1 or p == n - 1 or a % n == 0:
            continue
        for _ in range(s):
            prev = p
            p = (p * p) % n
            if p == 1:
                return gcd(prev - 1, n)
            if p == n - 1:
                break
        else:
            for i in range(2, n):
                x, y = i, (i * i + 1) % n
                f = gcd(abs(x - y), n)
                while f == 1:
                    x, y = (x * x + 1) % n, (y * y + 1) % n
                    y = (y * y + 1) % n
                    f = gcd(abs(x - y), n)
                if f != n:
                    return f
    return n


@memodict
def prime_factors(n):
    """returns a Counter of the prime factorization of n"""
    if n <= 1:
        return Counter()
    f = pollard_rho(n)
    return Counter([n]) if f == n else prime_factors(f) + prime_factors(n // f)


def distinct_factors(n):
    """returns a list of all distinct factors of n"""
    factors = [1]
    for p, exp in prime_factors(n).items():
        factors += [p**i * factor for factor in factors for i in range(1, exp + 1)]
    return factors


def get_factors(n):
    """returns a sorted list of all distinct factors of n"""
    small, large = [], []
    for i in range(1, int(n**0.5) + 1, 2 if n & 1 else 1):
        if not n % i:
            small.append(i)
            large.append(n // i)
    if small[-1] == large[-1]:
        large.pop()
    large.reverse()
    small.extend(large)
    return small



def isPrime(n):
    if n <= 3: return n > 1
    if n & 1 == 0 or n % 3 == 0: return False
    for i in range(5, int(n**0.5)+2, 6):
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

def all_factors(f, fac, primes, ind, arr, cnt):
    if cnt[0] == -1:
        return
    if ind == len(primes):
        if f != 1:
            if BS(arr, f) != -1:
                cnt[0] += 1
            else:
                cnt[0] = -1
        return
    maxpow = fac[primes[ind]]
    for pow in range(maxpow + 1):
        f *= primes[ind] ** pow
        all_factors(f, fac, primes, ind + 1, arr, cnt)
        f //= primes[ind] ** pow
    
    





# Tutorial Method
def main():
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]
        arr.append(1)
        arr.sort()
        num = arr[1] * arr[-1]
        arr.append(num)
        factors_lst = get_factors(num)
        if factors_lst == arr:
            print(num)
        else:
            print(-1)







# My method
def main1():
    TestCases = 1
    TestCases = int(input())
    sieve()
    for _ in range(TestCases):
        # n,k = [int(i) for i in input().split()]
        n = int(input())
        arr = [int(i) for i in input().split()]
        # s = input()
        arr.sort()

        primes = [i for i in arr if is_prime[i]]

        if not primes:
            print(-1)
            continue

        fac = defaultdict(int)

        nof = 1
        ans = 1
        for p in primes:
            pow = 0
            cur = p
            while BS(arr, cur) != -1:
                pow += 1
                cur *= p

            nof *= pow + 1
            ans *= cur // p
            fac[p] = pow
        
        if ans in arr:
            if len(fac) > 1:
                print(-1)
            else:
                p = list(fac.keys())[0]
                ans *= p
                a2 = [p]
                for i in range(fac[p] - 1):
                    a2.append(p * a2[-1])
                if a2 == arr:
                    print(ans)
                else:
                    print(-1)
            continue

        # print(fac)
        arr.append(ans)
        cnt = [0]
        all_factors(1, fac, primes, 0, arr, cnt)
        # print(a2 == arr)
        if cnt[0] == len(arr):
            print(ans)
        else:
            print(-1)
        


        # while ans in arr:
        #     ans *= arr[0]
        #     nof //= fac[arr[0]] + 1
        #     fac[arr[0]] += 1
        #     nof *= fac[arr[0]] + 1
        # print(dict(fac))
        # print(ans)


        
        









        # l = arr[0]
        # for i in range(1, n):
        #     l = lcm(l, arr[i])
        
        # num = l
        # if num in arr:
        #     num *= arr[0]

        # ans = num
        # # fac = prime_factors(num)
        # # nof = 1
        # # print(num, fac)

        # # for f, p in fac.items():
        # #     nof *= p + 1
        # primes = primesbelow(int(num**.5)+10)
        # nof = 1
        # for p in primes:
        #     pow = 0
        #     while num % p == 0:
        #         num //= p
        #         pow += 1
        #     nof *= pow + 1
        
        # if num > 1:
        #     nof *= 2


        # if nof - 2 == n:
        #     print(ans)
        # else:
        #     print(-1)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# =============================== Region Fastio ===============================
if not os.path.isdir('C:/users/acer'):
    BUFSIZE = 8192
    
    
    class FastIO(IOBase):
        newlines = 0
    
        def __init__(self, file):
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

# =============================== Endregion ===============================

if __name__ == "__main__":
    #read()
    main()
    #dmain()

