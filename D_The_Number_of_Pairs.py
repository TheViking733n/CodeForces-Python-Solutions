from __future__ import division, print_function
import os,sys
from io import BytesIO, IOBase
from random import randint, randrange
if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip


from math import ceil, floor, factorial, log10
# from math import log,sqrt,cos,tan,sin,radians
from bisect import bisect_left, bisect_right
from collections import deque, Counter, defaultdict
# from bisect import bisect,bisect_left,bisect_right,insort,insort_left,insort_right
# from decimal import *
# from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace
# from collections import OrderedDict
# from itertools import permutations


M=1000000007
# M=998244353
# INF = float("inf")
INF = 9223372036854775807
PI = 3.141592653589793
R = randrange(2, 1 << 32)
# R = 0          # Enable this for debugging of dict keys in myDict

# ========================= Main ==========================

from functools import lru_cache

# @lru_cache(maxsize=None)
# def isPrimeMR(n):
#     d = n - 1
#     d = d // (d & -d)
#     L = [2, 7, 61] if n < 1<<32 else [2, 3, 5, 7, 11, 13, 17] if n < 1<<48 else [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
#     # L = [2, 3, 5, 7, 11, 13, 17]
#     if n in L:
#         return 1
#     for a in L:
#         t = d
#         y = pow(a, t, n)
#         if y == 1: continue
#         while y != n - 1:
#             y = (y * y) % n
#             if y == 1 or t == n - 1: return 0
#             t <<= 1
#     return 1
 
# @lru_cache(maxsize=None)
# def findFactorRho(n):
#     from math import gcd
#     m = 1 << n.bit_length() // 8
#     for c in range(1, 99):
#         f = lambda x: (x * x + c) % n
#         y, r, q, g = 2, 1, 1, 1
#         while g == 1:
#             x = y
#             for i in range(r):
#                 y = f(y)
#             k = 0
#             while k < r and g == 1:
#                 ys = y
#                 for i in range(min(m, r - k)):
#                     y = f(y)
#                     q = q * abs(x - y) % n
#                 g = gcd(q, n)
#                 k += m
#             r <<= 1
#         if g == n:
#             g = 1
#             while g == 1:
#                 ys = f(ys)
#                 g = gcd(abs(x - ys), n)
#         if g < n:
#             if isPrimeMR(g): return g
#             elif isPrimeMR(n // g): return n // g
#             return findFactorRho(g)
 
# @lru_cache(maxsize=None)
# def primeFactor(n):
#     i = 2
#     ret = {}
#     rhoFlg = 0
#     while i*i <= n:
#         k = 0
#         while n % i == 0:
#             n //= i
#             k += 1
#         if k: ret[i] = k
#         i += 1 + i % 2
#         if i == 101 and n >= 2 ** 20:
#             while n > 1:
#                 if isPrimeMR(n):
#                     ret[n], n = 1, 1
#                 else:
#                     rhoFlg = 1
#                     j = findFactorRho(n)
#                     k = 0
#                     while n % j == 0:
#                         n //= j
#                         k += 1
#                     ret[j] = k
 
#     if n > 1: ret[n] = 1
#     if rhoFlg: ret = {x: ret[x] for x in sorted(ret)}
#     return len(ret)

MAX_N = int(2e7) + 5                                                            
sp = [-1] * MAX_N    # Smallest prime of a number, for a prime p, sp[p] = p     
def init_sp():                                                                  
    for i in range(2, MAX_N, 2):                                                
        sp[i] = 2    # For all even no., its sp will be 2                       
                                                                                
    for i in range(3, MAX_N, 2):  # Now for odd numbers                         
        if sp[i] == -1:                                                         
            sp[i] = j = i                                                       
            while j * i < MAX_N:                                                
                if sp[j * i] == -1:                                             
                    sp[j * i] = i                                               
                j += 2    

# memo1 = {}                                                
# def primeFactor(n):       
#     if n in memo1: return memo1[n]                                                        
#     seen = set()                    
#     while n != 1:                                                               
#         seen.add(sp[n] ^ R)                                                         
#         n //= sp[n]                                                             
#     memo1[n] = len(seen)
#     return len(seen)
                               
init_sp()   
                                                                    
memo1 = [0] * MAX_N
for i in range(2, MAX_N):
    prev = i // sp[i]
    memo1[i] = memo1[prev] + (sp[i] != sp[prev])
                                                                                

memo2 = {}
def divisors(n):
    if n in memo2: return memo2[n]
    divs = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            j = n // i
            divs.append(i)
            if i != j: divs.append(j)
    memo2[n] = divs
    return divs

# print(len(divisors(8648640)))

def main():
    TestCases = 1
    TestCases = int(input())
    """
    (ak - b) * G = c
    GCD(x, y) = G
    LCM(x, y) = k * G
    """
    
    for _ in range(TestCases):
        a, b, c = [int(i) for i in input().split()]
        
        ans = 0
        for p in divisors(c):
            # g = q = c // p
            if (p + b) % a == 0:
                k = (p + b) // a  # lcm = k * g
                pf = memo1[k]
                ans += 1 << pf

                # for r in range(1, k + 1):
                #     if k % r: continue
                #     s = k // r
                #     if s < r: break
                #     # r and s must be coprime
                #     if gcd(r, s) != 1: continue
                #     ans.add((r * g, s * g))
                #     ans.add((s * g, r * g))
                
        print(ans)
        # print(len(ans))
                

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# ======================== Functions declaration Starts ========================
abc='abcdefghijklmnopqrstuvwxyz'
abd={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}

def copy2d(lst): return [x[:] for x in lst]   #Copy 2D list... Avoid Using Deepcopy
def no_of_digits(num): return 0 if num <= 0 else int(log10(num)) + 1
def powm(num, power, mod=M): return pow(num, power, mod)
def isPowerOfTwo(x): return (x and (not(x & (x - 1))))
def LSB(num):
    """Returns Least Significant Bit of a number (Rightmost bit) in O(1)"""
    return num & -num

def MSB(num):
    """Returns Most Significant Bit of a number (Leftmost bit) in O(logN)"""
    if num <= 0: return 0
    ans = 1; num >>= 1
    while num:
        num >>= 1; ans <<= 1
    return ans


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
            
# =============================== Custom Classes ===============================

class Wrapper(int):
    def __init__(self, x):
        int.__init__(x)
    def __hash__(self):
        return super(Wrapper, self).__hash__() ^ R
Int = lambda x:Wrapper(int(x))        

class myDict():
    def __init__(self,func=int):
        # self.RANDOM = randint(0,1<<32)
        self.RANDOM = R
        self.default=func
        self.dict={}
    def __getitem__(self,key):
        myKey=self.RANDOM^key
        if myKey not in self.dict:
            self.dict[myKey]=self.default()
        return self.dict[myKey]
    def __setitem__(self,key,item):
        myKey=self.RANDOM^key
        self.dict[myKey]=item
    def __contains__(self,key):
        myKey=self.RANDOM^key
        return myKey in self.dict
    def __delitem__(self,key):
        myKey=self.RANDOM^key
        del self.dict[myKey]
    def keys(self):
        return [self.RANDOM^i for i in self.dict]


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
