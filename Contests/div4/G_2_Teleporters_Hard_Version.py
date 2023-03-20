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
INF = float("inf")
PI = 3.141592653589793
R = randrange(2, 1 << 32)
# R = 0          # Enable this for debugging of dict keys in myDict

# ========================= Main ==========================


def main():
    TestCases = 1
    TestCases = int(input())
    
    for _ in range(TestCases):
        n, c = [int(i) for i in input().split()]
        c1 = c
        # n = int(input())
        arr = [int(i) for i in input().split()]
        # s = input()

        left = [arr[i] + i + 1 for i in range(n)]
        right = [arr[i] + n-i for i in range(n)]

        # print(left)
        # print(right)

        # a2 = []
        # for i in range(n):
        #     if left[i] <= right[i]:
        #         a2.append((left[i], True))
        #     else:
        #         a2.append((right[i], False))
            
        # a2.sort()


        # i = 0
        # leftTaken = False
        # ans = 0
        # while i < n:
        #     if c - a2[i][0] >= 0:
        #         if a2[i][1]:
        #             leftTaken = True
        #         c -= a2[i][0]
        #         i += 1
        #         ans += 1
        #     else:
        #         break

        # if leftTaken:
        #     print(ans)
        #     continue

        # print(">>> ", end = '')

        c = c1

        a2 = [(min(left[i], right[i]), left[i]) for i in range(n)]
        a2.sort()

        # print(left)
        # print(right)
        # print(a2)

        ps = [0]
        for i in range(n):
            ps.append(ps[-1]+a2[i][0])
        # ps = ps[1:]
        # print(ps)
        # ps.append(0)
        
        ans = 0
        if min(left) <= c:
            ans = 1

        for i in range(n):
            mn, l = a2[i]

            x = 1
            coin = c - l
            if coin <= 0:
                continue

            
            low = 0
            high = n
            while low <= high:
                mid = (low + high) // 2
                price = ps[mid]
                cnt = mid + 1
                if mid > i:
                    price -= mn
                    cnt -= 1
                if price <= coin:
                    low = mid + 1
                    x = cnt
                else:
                    high = mid - 1

            

            # if i > 0 and ps[i-1] < coin:
            #     ind = bisect_right(ps, coin)
            #     x += ind
            # else:
            #     coin += mn
            #     ind = bisect_right(ps, coin)
            #     x = ind
            
            ans = max(ans, x)

        print(ans)

            














        # seg = SegmentTree([i[0] for i in a2], func=lambda x,y: x + y)

        # ans = 0
        # if min(left) <= c:
        #     ans = 1

        # for i in range(n):
        #     mn, l = a2[i]
        #     seg[i] = 0
        #     coin = c - l
        #     if coin <= 0:
        #         continue

        #     low = 0
        #     high = n-1
        #     ind = -1
        #     while low < high:
        #         mid = (low + high) // 2
        #         if seg.query(0, mid+1) <= coin:
        #             low = mid + 1
        #             ind = mid
        #         else:
        #             high = mid - 1
            
        #     x = ind + 1
        #     if ind < i:
        #         x += 1
            
        #     ans = max(ans, x)
        #     seg[i] = mn
        
        # print(ans)
            
                







        # ps = [0]
        # for i in range(n):
        #     ps.append(ps[-1]+a2[i][0])
        # # print(ps)
        # ps = ps[1:]
        
        # ans = 0
        # if min(left) <= c:
        #     ans = 1

        # for i in range(n):
        #     # taken = ps[i]
        #     # taken += left[i]

        #     l = a2[i][1]
        #     mnn = a2[i][0]
        #     # coin = c - (left[i] - a2[i])
        #     coin = c - l
        #     x = 0
        #     if coin <= 0:
        #         continue

        #     ind = bisect_right(ps, coin)
        #     if ind <= i:
        #         coin += mnn
        #         ind = bisect_right(ps, coin)

        #     x += ind

        #     if ind <= i:
        #         x -= 1
            

            # low = 0
            # high = n

            
            # x = 0
            # while low < high:
            #     mid = (low + high) // 2
            #     if ps[mid+1] <= coin:
            #         low = mid + 1
            #         x = mid + 1
            #     else:
            #         high = mid
            # print(i, x, coin)
            
        #     ans = max(ans, x)
        
        # print(ans)

            























        # # mn = min(left)
        # mn = INF
        # for i in range(n):
        #     if right[i] < left[i]:
        #         continue
        #     mn = min(left[i], right[i])
        # if mn == INF:
        #     mn = min(left)
        # c -= mn
        # if c<0:
        #     mn2 = min(left)
        #     c = c1
        #     c -= mn2
        #     if c < 0:
        #         print(0)
        #     else:
        #         print(1)
        #     continue
        
        # mxright = -INF
        # ind = -1

        # for i in range(n):
        #     if left[i] == mn:
        #         if right[i] > mxright:
        #             ind = i
        #             mxright = right[i]
        
        # left[ind] = right[ind] = INF

        # a2 = []
        # for i in range(n):
        #     if left[i] <= right[i]:
        #         a2.append((left[i], True))
        #     else:
        #         a2.append((right[i], False))

        # a2.sort()
        # i = 0
        # ans = 1
        # while i < n:
        #     if c - a2[i][0] >= 0:
        #         c -= a2[i][0]
        #         i += 1
        #         ans += 1
        #     else:
        #         break

        # print(ans)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
