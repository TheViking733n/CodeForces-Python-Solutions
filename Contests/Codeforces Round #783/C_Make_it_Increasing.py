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
from itertools import chain
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


def main():
    TestCases = 1

    for _ in range(TestCases):
        n = int(input())
        arr = [int(i) for i in input().split()]
        
        ans = INF
        for i in range(n):
            # Positive side
            prev = 0
            c1 = 0
            for j in range(i+1,n):
                cur = arr[j]
                k = (prev+cur-(prev%cur))//cur
                c1 += k
                prev = k*cur
            
            # Negative side
            prev = 0
            c2 = 0
            for j in range(i-1,-1,-1):
                cur = arr[j]
                k = (prev+cur-(prev%cur))//cur
                c2 += k
                prev = k*cur
            
            ans = min(ans,c1+c2)
        
        print(ans)


























































# def solve(k0, arr, n, opt=False):
#     ans = abs(k0)
#     brr = [k0*arr[0]]
#     cnt = [ans]

#     ans = cnt[0]

#     prev = brr[0]


#     for i in range(1,n):
#         cur = abs(arr[i])
#         # sgn = -1 if cur<0 else 1
#         k = (prev+cur-(prev%cur))//cur 
    
#         # cnt.append(abs(k))
#         ans += abs(k)
#         # print(k)
#         prev = cur*k
#         brr.append(prev)
    
    
#     if prev<0:
#         ans -= abs(prev//arr[-1])
#         brr[-1] = 0


#     # optimization
#     if opt:
#         for i in range(n-1,0,-1):
#             b1,b2 = brr[i-1], brr[i]
#             a1,a2 = arr[i-1], arr[i]
#             if b1>0 or b2>0: continue
#             if b1+a1<b2:
#                 k = (b2-b1)//a1 - 1
#                 b1 += k*a1
            
#                 while b1+a1<b2:
#                     b1 += a1
#                     k += 1
                
#                 ans -= k
#                 brr[i-1] = b1
#                 # cnt[i-1] -= abs(k)


#         # if b2<0:
#         #     ans -= abs(b2//a2)
        

    
#     # print(brr)
#     # print(cnt)
#     return ans

# def main():
#     TestCases = 1
#     # TestCases = int(input())

#     for _ in range(TestCases):
#         # n,k = [int(i) for i in input().split()]
#         n = int(input())
#         arr = [int(i) for i in input().split()]
#         # s = input()

#         low = -int(1.5e9/arr[0])
#         high = 0

#         # print(solve(-1,arr,n))

#         ans = INF
#         a1 = ans

#         while low<=high:
#             mid = (low+high)//2
#             a = solve(mid,arr,n)
#             # print(a)
#             if a<ans:
#                 ans = a
#                 a1 = solve(mid,arr,n,True)
#                 low = mid+1
#             else:
#                 high = mid-1
        
#         print(a1)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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

