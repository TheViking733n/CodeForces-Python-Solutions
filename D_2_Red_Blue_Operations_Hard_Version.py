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


# class FenwickTree:
#     def __init__(self, x):
#         """transform list into BIT"""
#         self.arr = x
#         x = self.bit = x[:]
#         for i in range(len(x)):
#             j = i | (i + 1)
#             if j < len(x):
#                 x[j] += x[i]

#     def update(self, idx, x):
#         """updates bit[idx] += x"""
#         self.arr[idx] += x
#         while idx < len(self.bit):
#             self.bit[idx] += x
#             idx |= idx + 1

#     def __getitem__(self, idx):
#         return self.arr[idx]
    
#     def __setitem__(self, idx, x):
#         """updates bit[idx] = x"""
#         self.update(idx, x - self.arr[idx])
    
#     def __iadd__(self, idx, x):
#         """updates bit[idx] += x"""
#         self.update(idx, x)


#     def sum(self, end):
#         """calc sum from [0, end) (zero based)"""
#         x = 0
#         while end > 0:
#             x += self.bit[end - 1]
#             end &= end - 1
#         return x
    
#     def query(self, begin, end):
#         """calc sum from [begin, end) (zero based)"""
#         if begin >= end:
#             return 0
#         return self.sum(end) - self.sum(begin)

#     def findkth(self, k):
#         """Find largest idx such that sum from [0, idx) <= k"""
#         idx = -1
#         for d in reversed(range(len(self.bit).bit_length())):
#             right_idx = idx + (1 << d)
#             if right_idx < len(self.bit) and k >= self.bit[right_idx]:
#                 idx = right_idx
#                 k -= self.bit[idx]
#         return idx + 1
    
#     def __repr__(self):
#         return "BIT({})".format(self.arr)


# class RangeUpdatePointQuery:
#     def __init__(self, arr):
#         self.arr = arr
#         self.bit = FenwickTree([0] * (len(arr) + 1))
    
#     def update(self, l, r, x):
#         """updates arr[l:r] += x"""
#         self.bit.update(l, x)
#         self.bit.update(r, -x)
    
#     def __getitem__(self, idx):
#         return self.arr[idx] + self.bit.sum(idx+1)
    
#     def __repr__(self):
#         return "RUPQ({})".format([self[i] for i in range(len(self.arr))])

# def getMinTernarySearch(arr, n):
#     low, high = 0, n - 1
#     while low <= high:
#         m1 = low + (high - low) // 3
#         m2 = high - (high - low) // 3
#         if arr[m1] > arr[m2]:
#             low = m1 + 1
#         else:
#             high = m2 - 1
#     return arr[low]

class LazySegmentTree:
    def __init__(self, data, default=0, func=min):
        """initialize the lazy segment tree with data"""
        self._default = default
        self._func = func

        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()
        self._lazy = [0] * (2 * _size)

        self.data = [default] * (2 * _size)
        self.data[_size:_size + self._len] = data
        for i in reversed(range(_size)):
            self.data[i] = func(self.data[i + i], self.data[i + i + 1])

    def __len__(self):
        return self._len

    def _push(self, idx):
        """push query on idx to its children"""
        # Let the children know of the queries
        q, self._lazy[idx] = self._lazy[idx], 0

        self._lazy[2 * idx] += q
        self._lazy[2 * idx + 1] += q
        self.data[2 * idx] += q
        self.data[2 * idx + 1] += q

    def _update(self, idx):
        """updates the node idx to know of all queries applied to it via its ancestors"""
        for i in reversed(range(1, idx.bit_length())):
            self._push(idx >> i)

    def _build(self, idx):
        """make the changes to idx be known to its ancestors"""
        idx >>= 1
        while idx:
            self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1]) + self._lazy[idx]
            idx >>= 1

    def add(self, start, stop, value):
        """lazily add value to [start, stop)"""
        start = start_copy = start + self._size
        stop = stop_copy = stop + self._size
        while start < stop:
            if start & 1:
                self._lazy[start] += value
                self.data[start] += value
                start += 1
            if stop & 1:
                stop -= 1
                self._lazy[stop] += value
                self.data[stop] += value
            start >>= 1
            stop >>= 1

        # Tell all nodes above of the updated area of the updates
        self._build(start_copy)
        self._build(stop_copy - 1)

    def query(self, start, stop, default=INF):
        """func of data[start, stop)"""
        start += self._size
        stop += self._size

        # Apply all the lazily stored queries
        self._update(start)
        self._update(stop - 1)

        res = default
        while start < stop:
            if start & 1:
                res = self._func(res, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res = self._func(res, self.data[stop])
            start >>= 1
            stop >>= 1
        return res

    def __repr__(self):
        return "LazySegmentTree({0})".format([self.query(i, i + 1) for i in range(self._len)])

def solve(n, k, a2, etc, negones):
    idx = bisect_right(etc, negones) - 1
    bars = idx + 1
    height = a2[idx]
    negones -= etc[idx]
    return k - n + min(a2[-1], height - (negones + bars - 1) // bars)

def main():
    TestCases = 1
    
    for _ in range(TestCases):
        n, q = [int(i) for i in input().split()]
        arr = [int(i) for i in input().split()]
        queries = [int(i) for i in input().split()]
        arr.sort()

        if n == 1:
            print(*[arr[0] - (k >> 1) + k * (k & 1) for k in queries])
            continue

        # rupq = RangeUpdatePointQuery(arr)
        seg = LazySegmentTree(arr)
        cache = [0] * (n + 1)
        for i in range(n):
            # rupq.update(0, i+1, 1)
            # cache[i+1] = getMinTernarySearch(rupq, n)
            seg.add(0, i+1, 1)
            cache[i+1] = seg.query(0, n)

        a2even = [arr[i] + n - i for i in range(n)]
        a2odd = a2even[:-1]; last = arr[-1]
        a2even.sort(reverse=True)
        a2odd.sort(reverse=True)
        sm, etcEven = 0, []
        for i in range(n):
            sm += a2even[i]
            etcEven.append(sm - (i + 1) * a2even[i])

        sm, etcOdd = 0, []
        for i in range(n-1):
            sm += a2odd[i]
            etcOdd.append(sm - (i + 1) * a2odd[i])

        ans = []
        for k in queries:
            if k <= n:
                ans.append(cache[k])
                continue
            
            if k - n + 1 & 1: # Even case
                negones = k - n + 1 >> 1
                ans.append(solve(n, k, a2even, etcEven, negones))
                continue

            # Odd case
            totalnegones = k - n + 1 >> 1
            low, high = 0, totalnegones
            while low < high:
                m1 = low + (high - low) // 3
                m2 = high - (high - low) // 3
                v1 = min(last - m1, solve(n, k, a2odd, etcOdd, totalnegones - m1))
                v2 = min(last - m2, solve(n, k, a2odd, etcOdd, totalnegones - m2))
                if v1 <= v2:
                    low = m1 + 1
                else:
                    high = m2 - 1
            # ans.append(max((min(last - i, solve(n, k, a2odd, etcOdd, totalnegones - i))) for i in range(low, low+1) if 0 <= i <= totalnegones))
            ans.append(min(last - low, solve(n, k, a2odd, etcOdd, totalnegones - low)))


        
        print(*ans)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
