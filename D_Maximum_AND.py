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

# def f(a, b, bit):
#     if bit <= -1: return 0, 0
#     n = len(a)
#     if n == 0: return 0, 0
#     a0, a1, b0, b1 = [], [], [], []
#     for i in range(n):
#         if a[i] & (1 << bit): a1.append(a[i])
#         else: a0.append(a[i])
#         if b[i] & (1 << bit): b1.append(b[i])
#         else: b0.append(b[i])
    
#     x = (1 << bit) - 1
#     # ans1, ans2 = f([i & x for i in a], [i & x for i in b], bit - 1)
#     ans1, ans2 = f(a, b, bit - 1)
#     if len(a0) != len(b1):
#         return ans1, ans2
    
#     if not a0:
#         return (1 << bit) | f(a1, b1, bit - 1)[0], ans1
#     if len(a0) == len(b1):
#         u1, u2 = f(a0, b1, bit - 1)
#         v1, v2 = f(a1, b0, bit - 1)
#         ans2 = ans1
#         if a0 and a1:
#             ans1 = (1 << bit) | max([u1 & v1, u1 & v2, u2 & v1, u2 & v2])
#         elif a0:
#             ans1 = (1 << bit) | u1
#         else:
#             ans1 = (1 << bit) | v1

#     return ans1, ans2


# def f(a, b, bit):
#     n = len(a)
#     if n == 0:
#         return 0
#     if bit <= 0:
#         # print(a, b)
#         # a = sorted(a)
#         # b = sorted(b, reverse=True)
#         x = a[0] ^ b[0]
#         for i in range(1, n):
#             x &= a[i] ^ b[i]
#         return x
#         # return 0
    
#     a0, a1, b0, b1 = [], [], [], []
#     for i in range(n):
#         if a[i] & (1 << bit): a1.append(a[i])
#         else: a0.append(a[i])
#         if b[i] & (1 << bit): b1.append(b[i])
#         else: b0.append(b[i])
#     # print(bit, a0, a1, b0, b1)
#     if len(a0) != len(b1):
#         x = (1 << bit) - 1
#         # return f([i & x for i in a], [i & x for i in b], bit - 1)
#         return f(a, b, bit - 1)

#     if not a1:
#         return f(a0, b1, bit - 1)

#     if not a0:
#         return f(a1, b0, bit - 1)

#     return max([f(a0, b1, i) & f(a1, b0, i) for i in range(-1, bit)])
#     # ans = 0
#     # for i in range(bit - 1, -1, -1):
#     #     ans = f(a0, b1, i) & f(a1, b0, i)
#     #     if ans & (1 << i):
#     #         break
#     # if not ans:
#     #     ans = f(a0, b1, -1) & f(a1, b0, -1)
#     # return ans



def f(a, b, bit):
    n = len(a)
    a0, a1, b0, b1 = [], [], [], []
    for i in range(n):
        if a[i] & (1 << bit): a1.append(a[i])
        else: a0.append(a[i])
        if b[i] & (1 << bit): b1.append(b[i])
        else: b0.append(b[i])
    
    if bit <= 0:
        return int(len(a0) == len(b1))
    
    if len(a0) != len(b1) or not a0 or not a1:
        x = (1 << bit) - 1
        return f([i & x for i in a], [i & x for i in b], bit - 1)
    
    ans = 0
    for j in range(bit):
        x = (1 << (j+1)) - 1
        ans = max(ans,
            f([i & x for i in a0], [i & x for i in b1], j) & 
            f([i & x for i in a1], [i & x for i in b0], j)
        )

    return (1 << bit) | ans



def main():
    TestCases = 1
    TestCases = int(input())
    test2 = TestCases == 10000
    
    for test in range(TestCases):
        # n, k = [int(i) for i in input().split()]
        n = int(input())
        a = [int(i) for i in input().split()]
        b = [int(i) for i in input().split()]
        # if test2 and test == 3194:
        #     print(n)
        #     print(*a)
        #     print(*b)
        #     continue
        # if test2:
        #     continue
        # s = input()
        print(f(a, b, 30))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
