from __future__ import division, print_function
import os,sys
from io import BytesIO, IOBase

if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip




from math import ceil, floor, factorial, sqrt
# from math import log,sqrt,cos,tan,sin,radians
from bisect import bisect_left, bisect_right
from collections import defaultdict
from collections import deque, Counter, OrderedDict
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
    
# ========================= Functions declaration Ends =========================

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

def primeFactors(n):
    # cnt = defaultdict(int)
    sm = 0
    if n==1:
        return sm
    while not n%2:
        # cnt[2]+=1
        sm += 1
        n = n // 2
    for i in range(3,int(sqrt(n))+1,2):
        while n % i== 0:
            # cnt[i] += 1
            sm += 1
            n = n // i
    if n > 2:
        # cnt[n] += 1
        sm += 1
    return sm

# def find_prime_factors(n):
#     """
#     Returns a dictionary with all prime factors of n.
#     """
#     return d

def main():
    TestCases = 1
    TestCases = int(input())
    # primes = primesbelow(int(10**(4.5)))

    # print(Counter(find_primes_factors(24)))
    for _ in range(TestCases):
        a,b,k = [int(i) for i in input().split()]
        
        if k==1:
            if a==b==1:
                print("NO")
                continue

            if (a%b==0 or b%a==0) and a!=b:
                print("YES")
                continue

            print("NO")
            continue

        # A = defaultdict(int)
        # B = defaultdict(int)
        # sm = 0
        # a11,b11 = a, b
        # for i in primes:
        #     while a11 % i == 0 and sm<k and a11>1:
        #         # A[i] += 1
        #         sm += 1
        #         a11 //= i
        #     while b11 % i == 0 and sm<k and b11>1:
        #         # B[i] += 1
        #         sm += 1
        #         b11 //= i
            
        #     if sm >= k or (a11==b11==1) or (i>a11 and i>b11):
        #         break

        sm = primeFactors(a) + primeFactors(b)

        # if a11>1:
        #     if isPrime(a11):
        #         sm += 1
        # if b11>1:
        #     if isPrime(b11):
        #         sm += 1

        kmax = sm
        print("YES" if k<=kmax else "NO")








        # a1 = A-B
        # b1 = B-A
        # print(a1)
        # print(b1)

        # cnt = 0 
        # for num,pow in a1.items():
        #     cnt += pow
        
        # for num,pow in b1.items():
        #     cnt += pow
        
        # if k < cnt:
        #     print("NO")
        #     continue

        # k -= cnt
        # if k&1:
        #     print("NO")
        #     continue

        # intersection = A - a1
        # for num, pow in intersection.items():
        #     k -= pow*2
        
        # if k <= 0:
        #     print("YES")
        # else:
        #     print("NO")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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