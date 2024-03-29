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
oo = 9223372036854775807
PI = 3.141592653589793
R = randrange(2, 1 << 32)
# R = 0          # Enable this for debugging of dict keys in myDict

# ========================= Main ==========================

class RangeQuery:
    def __init__(self, data, func=min):
        self.func = func
        self._data = _data = [list(data)]
        i, n = 1, len(_data[0])
        while 2 * i <= n:
            prev = _data[-1]
            _data.append([func(prev[j], prev[j + i]) for j in range(n - 2 * i + 1)])
            i <<= 1

    def query(self, start, stop):
        """func of data[start, stop)"""
        depth = (stop - start).bit_length() - 1
        return self.func(self._data[depth][start], self._data[depth][stop - (1 << depth)])

    def __getitem__(self, idx):
        return self._data[0][idx]



def f(st, en):
    if st >= en:
        return 0
    mn0, i1 = decode(rmn.query(st, en+1))
    mx0, i2 = decode(rmx.query(st, en+1))
    ans = 0
    '''
    Case - I:
    0 1 2 3 4 5 6 7 8
        L     R    
    l            r
    l      r      
            l     r
    '''
    if i1 < i2:
        left = i1 - st + 1
        mid = i2 - i1 - 1
        right = en - i2 + 1
        ans += left * right
        mx = -oo; mn = oo
        for i in range(i1 + 1, i2):
            mx = max(mx, arr[i])
            # Find leftmost index in [st, i1] such that max(arr[idx..i1]) < mx
            low, high = st, i1; idx = i1
            while low <= high:
                mid = low + high >> 1
                if (rmx.query(mid, i1+1)>>20) < mx:
                    high = mid - 1
                    idx = mid
                else:
                    low = mid + 1
            ans += i1 - idx + 1

        for i in range(i2 - 1, i1, -1):
            mn = min(mn, arr[i])
            # Find rightmost index in [i2, en] such that min(arr[i2..idx]) > mn
            low, high = i2, en; idx = i2
            while low <= high:
                mid = low + high >> 1
                if (rmn.query(i2, mid+1)>>20) > mn:
                    low = mid + 1
                    idx = mid
                else:
                    high = mid - 1
            ans += idx - i2 + 1
    
        '''
        Case - II:
        0 1 2 3 4 5 6 7 8
            R     L    
        l           r       -> No sol
        l     r
                l     r
            
        '''

    elif i1 > i2:
        i1, i2 = i2, i1
        mn = oo; mx = -oo
        for i in range(i1-1, st-1, -1):
            mn = min(mn, arr[i])
            # Find rightmost index in [i1, i2-1] such that min(arr[i1..idx]) > mn
            low, high = i1, i2-1; idx = i1
            while low <= high:
                mid = low + high >> 1
                if (rmn.query(i1, mid+1)>>20) > mn:
                    low = mid + 1
                    idx = mid
                else:
                    high = mid - 1
            ans += idx - i1 + 1

        for i in range(i2 + 1, en + 1):
            mx = max(mx, arr[i])
            # Find leftmost index in [i1+1, i2] such that max(arr[idx..i2]) < mx
            low, high = i1+1, i2; idx = i2
            while low <= high:
                mid = low + high >> 1
                if (rmx.query(mid, i2+1)>>20) < mx:
                    high = mid - 1
                    idx = mid
                else:
                    low = mid + 1
            ans += i2 - idx + 1

    ans += f(st, i1-1)
    ans += f(i1 + 1, i2 - 1)
    ans += f(i2+1, en)
    return ans

rmn = rmx = arr = n = tree = None


def encode(x, y): return x << 20 | y
def decode(z): return z >> 20, z & 0xfffff

def main():
    global rmn, rmx, arr, arr, n, tree
    n = int(input())
    arr = [int(i) - 1 for i in input().split()]
    a2 = [encode(arr[i], i) for i in range(n)]
    rmn = RangeQuery(a2, min)
    rmx = RangeQuery(a2, max)

    print(f(0, n-1))

    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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

