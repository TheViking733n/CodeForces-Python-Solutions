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
from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace
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

# import heapq

# class HeapPQ:
#     """
#     Only hashable key type is supported
#     """

#     def __init__(self):
#         self.pq = []
#         self.pq_set = set()
    
#     def push(self, priority, key):
#         if key not in self.pq_set:
#             heapq.heappush(self.pq, (priority, key))
#             self.pq_set.add(key)
#         else:
#             index = list(map(lambda x:x[1], self.pq)).index(key)
#             self.pq[index] = (priority, key)
#             heapq.heapify(self.pq)
    
#     def pop(self):
#         priority, key = heapq.heappop(self.pq)
#         self.pq_set.remove(key)
#         return priority, key
    
#     def empty(self) -> bool:
#         return len(self.pq) == 0

def main():
    TestCases = 1
    # n = 3000
    # arr = [int(1e9)] * n
    # arr = [i+int(1e9) for i in range(n)]
    # arr[0] = 1
    # arr[1] = 2
    # arr[3] = 10
    encode = lambda x, i: (x << 14) | i
    decode = lambda x: (x >> 14, x & ((1 << 14) - 1))
    for _ in range(TestCases):
        n = int(input())
        arr = [int(i) for i in input().split()]
        excess = []
        arr.sort()
        nxt = [-1] * n
        while n > 1:
            if arr[-1] == 0:
                excess.extend([0]*(n-1))
                break
            # if n > 1800: print(arr[:4], arr[-3:])
            avg = arr[0]
            excess.append(avg)
            arr = [arr[i] - avg for i in range(n)]
            newarr = []
            pq = [(arr[i]+arr[i+1], i) for i in range(min([int(n ** .5) + 2, n // 2, n - 1]))]
            heapify(pq)

            # pq = []
            # for i in range(min([int(n ** .5) + 2, n // 2, n - 1])):
            #     heappush(pq, (arr[i]+arr[i+1], i, i + 1))
            # for i in range(n - 1):
            #     val, idx1, idx2 = heappop(pq)
            #     newarr.append(val)
            #     if idx2 + 1 < n:
            #         idx2 += 1
            #         newval = (arr[idx1] + arr[idx2])
            #         heappush(pq, (newval, idx1, idx2))

            # pq = HeapPQ()
            for i in range(min([int(n ** .5) + 2, n // 2, n - 1])):
                # heappush(pq, encode(arr[i]+arr[i+1], i))
                # pq.push(arr[i]+arr[i+1], i)
                nxt[i] = i + 1
            # heapify(pq)
            for i in range(n - 1):
                val, idx1 = pq[0]
                newarr.append(val)
                nxt[idx1] += 1
                if nxt[idx1] < n:
                    newval = (arr[idx1] + arr[nxt[idx1]])
                    # heappush(pq, encode(newval, idx1))
                    # pq.push(newval, idx1)
                    heapreplace(pq, (newval, idx1))
            
            # print(newarr)
            arr = newarr
            n -= 1
        excess.reverse()
        # print(excess)
        ans = arr[0]
        cur = 2
        for i in excess:
            ans += i * cur
            ans %= M
            cur <<= 1
            while cur >= M:
                cur -= M
        print(ans)

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
