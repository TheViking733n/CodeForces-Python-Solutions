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

def fin_min(num, arr): # return index, diff
    d = abs(arr[0] - num)
    ind = 0
    for i in range(len(arr)):
        if d > abs(arr[i] - num):
            d = abs(arr[i] - num)
            ind = i
    return ind, d
    

def main():
    TestCases = 1
    TestCases = int(input())

    for _ in range(TestCases):
        # n,x,y = [int(i) for i in input().split()]
        n = int(input())
        a = [int(i) for i in input().split()]
        b = [int(i) for i in input().split()]
        # s = input()
        
        # a1 = sorted(a)
        # b1 = sorted(b)

        ans = INF
        
        # if n<=3:
        #     for i1 in range(n):
        #         for j1 in range(n):
        #                 for i2 in range(n):
        #                     for j2 in range(n):
        #                         if i1==i2 and j1==j2:
        #                             continue
        #                         ans = min(ans,abs(i1-j1)+abs(i2-j2), ans)


        # else:

        a1, a2, b1, b2 = a[0], a[-1], b[0], b[-1]

        wires = []
        # wire = [diff, id1, id2]

        ind, diff = fin_min(a1, b)
        if ind==0:
            id = 3
        elif ind==n-1:
            id = 4
        else:
            id = 0

        wire = [diff, 1, id]
        wires.append(wire)

        ind, diff = fin_min(a2, b)
        if ind==0:
            id = 3
        elif ind==n-1:
            id = 4
        else:
            id = 0
        
        wire = [diff, 2, id]
        wires.append(wire)


        ind, diff = fin_min(b1, a)
        if ind==0:
            id = 1
        elif ind==n-1:
            id = 2
        else:
            id = 0
            
        wire = [diff, id, 3]
        wires.append(wire)

        ind, diff = fin_min(b2, a)
        if ind==0:
            id = 1
        elif ind==n-1:
            id = 2
        else:
            id = 0

        wire = [diff, id, 4]
        wires.append(wire)

        wire = [abs(a1-b1), 1, 3]
        wires.append(wire)
        wire = [abs(a1-b2), 1, 4]
        wires.append(wire)
        wire = [abs(a2-b1), 2, 3]
        wires.append(wire)
        wire = [abs(a2-b2), 2, 4]
        wires.append(wire)


        # All subsequences of array using power set
        
        # array = "Hello"
        array = wires
        
        for i in range(1<<len(array)):
            # subseq = ""   # If array is string
            subseq = []     # If array is list; if array is string, it generates list of char
            for j in range(len(array)):
                if (i & (1<<j)) != 0:
                    # subseq += array[j]     # If array is string
                    subseq.append(array[j])  # If array is list
            cost = 0
            nodes = set()
            for wire in subseq:
                cost += wire[0]
                nodes.add(wire[1])
                nodes.add(wire[2])
            if 1 in nodes and 2 in nodes and 3 in nodes and 4 in nodes:
                ans = min(ans, cost)
            

        print(ans)


                
        
        

        
            




        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# =============================== Region Fastio ===============================

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

