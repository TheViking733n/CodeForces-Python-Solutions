# from _future_ import division, print_function
import os,sys
from io import BytesIO, IOBase
 
if sys.version_info[0] < 3:
    from _builtin_ import xrange as range
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
    
# ========================= Functions declaration Ends =========================
 
 # Python3 program to count numbers having 4 as a digit
import math as mt
 
# Function to count numbers from 1 to n
# that have 4 as a digit
def countNumbersWith4(n):
 
    # Base case
    if (n < 4):
        return 0
 
    # d = number of digits minus one in n.
    # For 328, d is 2
    d = int(mt.log10(n))
 
    # computing count of numbers from 1 to 10^d-1,
    # d=0 a[0] = 0
    # d=1 a[1] = count of numbers from 0 to 9 = 1
    # d=2 a[2] = count of numbers from
    #            0 to 99 = a[1]*9 + 10 = 19
    # d=3 a[3] = count of numbers from
    #            0 to 999 = a[2]*19 + 100 = 171
    a = [1 for i in range(d + 1)]
    a[0] = 0
    if len(a) > 1:
        a[1] = 1
    for i in range(2, d + 1):
        a[i] = a[i - 1] * 9 + mt.ceil(pow(10, i - 1))
 
    # Computing 10^d
    p = mt.ceil(pow(10, d))
 
    # Most significant digit (msd) of n,
    # For 328, msd is 3 which can be
    # obtained using 328/100
    msd = n // p
 
    # If MSD is 4. For example if n = 428,
    # then count of numbers is sum of following.
    # 1) Count of numbers from 1 to 399
    # 2) Count of numbers from 400 to 428 which is 29.
    if (msd == 4):
        return (msd) * a[d] + (n % p) + 1
 
    # IF MSD > 4. For example if n is 728,
    # then count of numbers is sum of following.
    # 1) Count of numbers from 1 to 399 and count
    #  of numbers from 500 to 699, i.e., "a[2] * 6"
    # 2) Count of numbers from 400 to 499, i.e. 100
    # 3) Count of numbers from 700 to 728, recur for 28
    if (msd > 4):
        return ((msd - 1) * a[d] + p +
                 countNumbersWith4(n % p))
 
    # IF MSD < 4. For example if n is 328,
    # then count of numbers is sum of following.
    # 1) Count of numbers from 1 to 299 a
    # 2) Count of numbers from 300 to 328, recur for 28
    return (msd) * a[d] + countNumbersWith4(n % p)
 
from datetime import datetime as dt

def main():
    t = int(1e4)
    # solved = {}
 
    while(t > 0):
        k = int(1e7)
        # if k in solved:
        #     print(solved[k])
        #     continue
        
        add = countNumbersWith4(k)
        prev = 0
        prevVal = add
        flag = True
        cnt = 0
        while(flag):
            # cnt += 1
            # if cnt > 1000:
            #     print(val1)
            #     st = dt.now()
            #     val1 = countNumbersWith4(k+add)
            #     print(dt.now() - st)    
            #     return
            val1 = countNumbersWith4(k+add)
            
            # val2 = countNumbersWith4(k+prev)
            val2 = prevVal
            if(val1 == val2):
                break
            
            else:
                prev = add
                prevVal = val1
                add += val1-val2
                if(val1 - val2 == 0):
                    break
        # solved[k] = add + k
        print(k+add)    
        t = t-1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# =============================== Region Fastio ===============================
if not os.path.isdir('C:/users/acer'):
    BUFSIZE = 8192
    
    
    class FastIO(IOBase):
        newlines = 0
    
        def _init_(self, file):
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
        def _init_(self, file):
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