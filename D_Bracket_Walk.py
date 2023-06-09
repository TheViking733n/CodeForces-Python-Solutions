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


class FenwickTree:
    def __init__(self, x):
        """transform list into BIT"""
        self.arr = x
        x = self.bit = x[:]
        for i in range(len(x)):
            j = i | (i + 1)
            if j < len(x):
                x[j] += x[i]

    def update(self, idx, x):
        """updates bit[idx] += x"""
        self.arr[idx] += x
        while idx < len(self.bit):
            self.bit[idx] += x
            idx |= idx + 1

    def __getitem__(self, idx):
        return self.arr[idx]
    
    def __setitem__(self, idx, x):
        """updates bit[idx] = x"""
        self.update(idx, x - self.arr[idx])
    
    def __iadd__(self, idx, x):
        """updates bit[idx] += x"""
        self.update(idx, x)


    def _sum(self, end):
        """calc sum from [0, end) (zero based)"""
        x = 0
        try:
            while end > 0:
                x += self.bit[end - 1]
                end &= end - 1
            return x
        except:
            print(end)
            exit(1)
    
    def query(self, begin, end):
        """calc sum from [begin, end) (zero based)"""
        if begin >= end:
            return 0
        return self._sum(end) - self._sum(begin)

    def findkth(self, k):
        """Find largest idx such that sum from [0, idx) <= k"""
        idx = -1
        for d in reversed(range(len(self.bit).bit_length())):
            right_idx = idx + (1 << d)
            if right_idx < len(self.bit) and k >= self.bit[right_idx]:
                idx = right_idx
                k -= self.bit[idx]
        return idx + 1
    
    def __repr__(self):
        return "BIT({})".format(self.arr)



class SortedMultiSet:
    def __init__(self, iterable=[], max_n=2 * 10**5):
        """Initialize sorted list instance."""
        self.N = max_n + 1
        self.fen = FenwickTree([0] * self.N)
        self.size = len(iterable)
        for x in iterable:
            self.fen.update(x, 1)
    
    def __getitem__(self, idx):
        """Lookup value at `idx`."""
        if not -self.size <= idx < self.size:
            raise IndexError("list index out of range")
        if idx < 0:
            idx += self.size
        return self.fen.findkth(idx + 1)
    
    def remove(self, x):
        """Remove first occurrence of value."""
        assert 0 <= x < self.N
        if self.fen[x] == 0:
            return False
        self.fen.update(x, -1)
        self.size -= 1
        return True

    def add(self, x):
        """Add value to sorted list."""
        assert 0 <= x < self.N
        self.fen.update(x, 1)
        self.size += 1

    def __contains__(self, x):
        """Return true if `x` in sorted list."""
        assert 0 <= x < self.N
        return self.fen[x] > 0
    
    def max(self):
        """Return max value in sorted list."""
        assert self.size > 0
        return self.fen.findkth(self.size-1)
    
    def min(self):
        """Return min value in sorted list."""
        assert self.size > 0
        return self.fen.findkth(0)
    
    def __len__(self):
        """Return the size of sorted list."""
        return self.size
    
    def __bool__(self):
        """Return `True` when sorted list is not empty."""
        return not self.size == 0

    def __repr__(self):
        """Return string representation of sorted list."""
        ans = []
        for i in range(self.N):
            ans.extend([i] * self.fen[i])
        return "SortedMultiSet({})".format(ans)
    




def main():
    TestCases = 1
    
    for _ in range(TestCases):
        n, q = [int(i) for i in input().split()]
        s = input()
        arr = [1 if i == '(' else -1 for i in s]

        if n == 2:
            for _ in range(q):
                pos = int(input()) - 1
                arr[pos] *= -1
                print("YES" if arr[0] == 1 and arr[1] == -1 else "NO")
            continue

        if n & 1:
            for _ in range(q):
                _ = input()
                print("NO")
            continue

        seg = FenwickTree(arr)
        
        plus = []
        minus = []
        for i in range(n-1):
            if arr[i] == 1 and arr[i+1] == 1:
                plus.append(i)
            elif arr[i] == -1 and arr[i+1] == -1:
                minus.append(i)
        
        plus = SortedMultiSet(plus, max_n=n)
        minus = SortedMultiSet(minus, max_n=n)

        for _ in range(q):
            pos = int(input()) - 1
            # print(plus, minus)
            if pos < n-1:
                if seg[pos] == 1 and seg[pos+1] == 1:
                    plus.remove(pos)
                elif seg[pos] == -1 and seg[pos+1] == -1:
                    minus.remove(pos)
                if seg[pos] == 1 and seg[pos+1] == -1:
                    minus.add(pos)
                elif seg[pos] == -1 and seg[pos+1] == 1:
                    plus.add(pos)
            if pos > 0:
                if seg[pos-1] == 1 and seg[pos] == 1:
                    plus.remove(pos-1)
                elif seg[pos-1] == -1 and seg[pos] == -1:
                    minus.remove(pos-1)
                if seg[pos-1] == 1 and seg[pos] == -1:
                    plus.add(pos-1)
                elif seg[pos-1] == -1 and seg[pos] == 1:
                    minus.add(pos-1)
            
            seg[pos] = -seg[pos]
            if len(plus):
                first = plus.min()
            else:
                first = INF
            if len(minus):
                last = minus.max()
            else:
                last = -INF
            
            tot = seg.query(0, n)
            
            if seg[0] == -1 or seg[n-1] == 1:
                print("NO")
                continue

            if first == INF:
                if last == INF:
                    print("YES" if tot == 0 else "NO")
                else:
                    print("YES" if tot >= 0 else "NO")
                continue

            if seg.query(0, first) < 0 or last != -INF and seg.query(last+2, n) > 0:
                print("NO")
                continue

            if tot & 1:
                print("NO")
                continue
            
            if first < last:
                print("YES")
                continue

            print("NO")



            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
