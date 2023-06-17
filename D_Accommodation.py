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
from itertools import permutations


M=1000000007
# M=998244353
# INF = float("inf")
oo = 9223372036854775807
PI = 3.141592653589793
R = randrange(2, 1 << 32)
# R = 0          # Enable this for debugging of dict keys in myDict

# ========================= Main ==========================
from functools import lru_cache

arr = None
@lru_cache(maxsize=None)
def DP(i, s):
    global arr
    if i <= 0: return (0, 0) if s == 0 else (oo, -oo)
    return (
        min(
            oo if i-2<0 else DP(i-2, s-1)[0] + (arr[i-1] | arr[i-2]),
            DP(i-1, s)[0] + arr[i-1]
        ),
        max(
            -oo if i-2<0 else DP(i-2, s-1)[1] + (arr[i-1] | arr[i-2]),
            DP(i-1, s)[1] + arr[i-1]
        )
    )
    

def brute(arr):
    n = len(arr)
    s, d = n >> 1, n >> 2
    seq = "1" * s + "2" * d
    mini, maxi = oo, -oo
    for p in set(permutations(seq)):
        p = [int(i) for i in p]
        ans = i = 0
        for cur in p:
            if cur == 1:
                ans += arr[i]
            elif cur == 2:
                ans += arr[i] | arr[i+1]
                i += 1
            i += 1
        mini = min(mini, ans)
        maxi = max(maxi, ans)
    return mini, maxi

def check(num):
    global arr
    b = bin(num)[2:]
    while len(b) % 4 != 0: b = "0" + b
    n, arr = len(b), [int(i) for i in b]
    # mn, mx = brute(arr)
    DP.cache_clear()
    mn, mx = DP(n, n >> 2)
    mn1, mx1 = minimize(b), maximize(b)
    if mn1 != mn:
        print(f"Minimize wrong: {b:>12} | Received: {mn1} | Expected: {mn}")
    if mx1 != mx:
        print(f"Maximize wrong: {b:>12} | Received: {mx1} | Expected: {mx}")


def checker():
    # for i in range(10 ** 6):
    for i in range(10 ** 6, 3 * 10 ** 7):
        print(i, end='\r', flush=1)
        check(i)
    # check(149503)
    check(4792319)
    exit()




def minimize(arr):
    n = len(arr)
    s, d = n >> 1, n >> 2
    a2 = arr.split('0')
    a2 = [len(i) for i in a2]
    ans = 0
    for i in range(len(a2)):
        while d > 0 and a2[i] > 1:
            d -= 1
            a2[i] -= 2
            ans += 1
        if d == 0: break
    return ans + sum(a2)



def _maximize(arr):
    n = len(arr)
    s, d = n >> 1, n >> 2

    ans = 0

    for i in range(0, n-1, 2):
        if d == 0: break
        if (arr[i], arr[i+1]) in ((1, 0), (0, 0)):
            ans += arr[i] | arr[i+1]
            arr[i], arr[i+1] = -2, 2
            d -= 1
        else:
            break

    for i in range(n-2, -1, -2):
        if d == 0: break
        if (arr[i], arr[i+1]) in ((0, 1), (0, 0)):
            ans += arr[i] | arr[i+1]
            arr[i], arr[i+1] = -2, 2
            d -= 1
        else:
            break

    for i in range(n-2):
        if d == 0: break
        if (arr[i+1], arr[i+2]) == (1, 0) and arr[i] != 0:
            arr[i+1], arr[i+2] = -2, 2
            d -= 1
            ans += 1
        elif (arr[i], arr[i+1]) == (0, 1) and arr[i+2] != 0:
            arr[i], arr[i+1] = -2, 2
            d -= 1
            ans += 1
    
    for i in range(n-1):
        if d == 0: break
        if (arr[i], arr[i+1]) == (0, 0):
            arr[i], arr[i+1] = -2, 2
            d -= 1

    for i in range(n-1):
        if d == 0: break
        if (arr[i], arr[i+1]) == (0, 1):
            arr[i], arr[i+1] = -2, 2
            d -= 1
            ans += 1
            if d > 0 and i+3 < n and (arr[i+2], arr[i+3]) == (1, 0):
                arr[i+2], arr[i+3] = -2, 2
                d -= 1
                ans += 1

    for i in range(n-1):
        if d == 0: break
        if (arr[i], arr[i+1]) == (1, 0):
            arr[i], arr[i+1] = -2, 2
            d -= 1
            ans += 1
            if d > 0 and i+3 < n and (arr[i+2], arr[i+3]) == (0, 1):
                arr[i+2], arr[i+3] = -2, 2
                d -= 1
                ans += 1
        
    for i in range(n-1):
        if d == 0: break
        if (arr[i], arr[i+1]) == (0, 1):
            arr[i], arr[i+1] = -2, 2
            d -= 1
            ans += 1

    for i in range(n-1):
        if d == 0: break
        if (arr[i], arr[i+1]) == (1, 0):
            arr[i], arr[i+1] = -2, 2
            d -= 1
            ans += 1

    for i in range(n-1):
        if d == 0: break
        if (arr[i], arr[i+1]) == (1, 1):
            arr[i], arr[i+1] = -2, 2
            d -= 1
            ans += 1

    return min((n >> 2) * 3, ans + sum(arr))


def _maximize2(arr):
    n = len(arr)
    s, d = n >> 1, n >> 2
    if arr.count(1) <= s: return arr.count(1)
    ans = 0
    for i in range(n - 1):
        if d == 0: break
        if (arr[i], arr[i+1]) in ((1, 0), (0, 1), (0, 0)):
            ans += arr[i] | arr[i+1]          
            arr[i], arr[i+1] = -2, 2
            d -= 1

    for i in range(n-1):
        if d == 0: break
        if (arr[i], arr[i+1]) == (1, 1):
            arr[i], arr[i+1] = -2, 2
            d -= 1
            ans += 1

    return min((n >> 2) * 3, ans + sum(arr))

            

def maximize(b):
    arr = [int(i) for i in b]
    # return max(_maximize(arr[:]), _maximize(arr[::-1]))
    return max(_maximize2(arr[:]), _maximize2(arr[::-1]))


def main():
    TestCases = 1
    # checker()
    
    for _ in range(TestCases):
        n, m = [int(i) for i in input().split()]
        mini = maxi = 0
        for _ in range(n):
            arr = input()
            x = minimize(arr)
            y = maximize(arr)
            mini += x
            maxi += y
            # print(arr, x, y)
        print(mini, maxi)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
