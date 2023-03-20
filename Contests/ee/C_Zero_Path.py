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
from types import GeneratorType


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc



@bootstrap
def dfs(x, y, grid, possible, n, m, sm):
    if x == n-1 and y == m-1:
        yield int(sm + grid[x][y] == 0)
    
    if possible[x][y][sm] != -1:
        yield possible[x][y][sm]
    
    cond1 = cond2 = 0
    if x+1<n:
        cond1 = yield dfs(x+1, y, grid, possible, n, m, sm + grid[x][y])
    
    if y+1<m:
        cond2 = yield dfs(x, y+1, grid, possible, n, m, sm + grid[x][y])

    possible[x][y][sm] = cond1 or cond2
    yield cond1 or cond2




def main():
    TestCases = 1
    TestCases = int(input())

    for _ in range(TestCases):
        n,m = [int(i) for i in input().split()]
        grid = [[int(i) for i in input().split()] for i in range(n)]

        path_len = n + m - 1
        if path_len & 1:
            print("NO")
            continue

        sums = [[defaultdict(int) for j in range(m)] for i in range(n)]
        sums[0][0] = [grid[0][0]]
        # arr = []
        for i in range(1,n):
            x, y = i, 0
            # st = set()
            while 0<=x<n and 0<=y<m:
                # st.add(grid[x][y])
                # print(x,y)

                x1, y1 = x-1, y
                x2, y2 = x, y-1
                st1 = []
                st2 = []
                if 0<=x1<n and 0<=y1<m:
                    st1 = sums[x1][y1]
                if 0<=x2<n and 0<=y2<m:
                    st2 = sums[x2][y2]
                    sums[x2][y2] = defaultdict(int)
                
                st = defaultdict(int)
                for nums in st1:
                    sums[x][y][nums+grid[x][y]] += 1
                for nums in st2:
                    sums[x][y][nums+grid[x][y]] += 1
                
                # sums[x][y] = list(st)

                x -= 1
                y += 1
                # if len(st)==2: break

            # arr.append(list(st))
        
        for j in range(1, m):
            x, y = n-1, j
            # st = set()
            while 0<=x<n and 0<=y<m:
                # st.add(grid[x][y])
                # print(x,y)

                x1, y1 = x-1, y
                x2, y2 = x, y-1
                st1 = []
                st2 = []
                if 0<=x1<n and 0<=y1<m:
                    st1 = sums[x1][y1]
                if 0<=x2<n and 0<=y2<m:
                    st2 = sums[x2][y2]
                    sums[x2][y2] = defaultdict(int)
                
                st = defaultdict(int)
                for nums in st1:
                    sums[x][y][nums+grid[x][y]] += 1
                for nums in st2:
                    sums[x][y][nums+grid[x][y]] += 1
                
                # sums[x][y] = list(st)


                x -= 1
                y += 1
                # if len(st)==2: break

            # arr.append(list(st))
        
        # print(len(arr))

        # cur = arr[0]

        # for i in range(1,len(arr)):
        #     c2 = set()
        #     for j in arr[i]:
        #         for val in cur:
        #             c2.add(val+j)
            
        #     cur = list(c2)
        
        # print(cur)
        print("YES" if 0 in sums[-1][-1] else "NO")
        # print(dict)
        
        
        
        
        
        
        
        # possible = [[defaultdict(lambda : -1) for j in range(m)] for i in range(n)]
        

        # print(possible[0][0][0])
        # ans = dfs(0, 0, grid, possible, n, m, 0)
        # print("YES" if ans else "NO")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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

