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
from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace
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
#     sys.setrecursionlimit(2005)
#     threading.stack_size(102400)
#     thread = threading.Thread(target=main)
#     thread.start()
    
# ========================= Functions declaration Ends =========================
solved = {}

# def f(ind, h, ans, arr):
#     if ind < 0:
#         return ans
    
#     if ind in solved and solved[ind] != 0:
#         return solved[ind]

#     # Not take
#     a1 = f(ind-1, h, ans, arr)

#     # Take
#     a2 = 0
#     if h+arr[ind]>=0:
#         a2 = f(ind-1, h+arr[ind], ans+1, arr)
    
#     solved[ind] = max(a1, a2)

#     return solved[ind]

# sys.setrecursionlimit(2005)
def main():
    TestCases = 1
    # TestCases = int(input())

    for _ in range(TestCases):
        # n,k = [int(i) for i in input().split()]
        n = int(input())
        arr = [int(i) for i in input().split()]
        # s = input()
        
        # arr.reverse()
        # a = f(n-1, 0, 0, arr)
        # print(a)
        # print(solved)
        

        # h11 = h12 = h21 = h22 = (0, 0)
        # for i in range(n):
        #     h21 = max(h11, h12) # Not take
        #     h = h21[1] + arr[i]
        #     h22 = h21 if h<0 else (h21[0]+1, h) # Take
        #     h11, h12 = h21, h22
        #     print(h11, h12)
        
        # print(max(h21, h22)[0])



        # dp1 = dp2 = dp3 = (0,0)
        # for i in range(n):
        #     dp3 = max(dp1, dp2)
        #     if dp3[1]+arr[i] >= 0:
        #         dp3 = (dp3[0]+1, dp3[1]+arr[i])
        #     print(i, arr[i], dp1, dp2, dp3, sep='\t')
        #     dp1, dp2 = dp2, dp3
        
        
        # print(max(dp1, dp2)[0])
        
        
        
        
        hq = []
        heapify(hq)
        h = 0
        for i in range(n):
            h += arr[i]
            heappush(hq, arr[i])
            if h<0:
                v = heappop(hq)
                h -= v
            
        print(len(hq))


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
    # dmain()

