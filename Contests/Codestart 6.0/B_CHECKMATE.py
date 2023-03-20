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

class DisjointSetUnion:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_sets = n

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a

            self.num_sets -= 1
            self.parent[b] = a
            self.size[a] += self.size[b]

    def set_size(self, a):
        return self.size[self.find(a)]

    def __len__(self):
        return self.num_sets


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b):
        self.parent[self.find(b)] = self.find(a)

def main():
    TestCases = 1
    # TestCases = int(input())
    
    for _ in range(TestCases):
        chess = [[i for i in input().split()] for _ in range(8)]
        # print(*chess, sep='\n')

        # dsu = DisjointSetUnion(64)
        danger = [[False] * 8 for i in range(8)]
        king, queen, rook, bishop, knight = [], [], [], [], []
        myking = None
        for i in range(8):
            for j in range(8):
                if chess[i][j] == 'k':
                    myking = (i, j)
                elif chess[i][j] == 'K':
                    king.append((i, j))
                elif chess[i][j] == 'Q':
                    queen.append((i, j))
                elif chess[i][j] == 'R':
                    rook.append((i, j))
                elif chess[i][j] == 'B':
                    bishop.append((i, j))
                elif chess[i][j] == 'N':
                    knight.append((i, j))
        
        for x, y in king:
            for i in range(8):
                for j in range(8):
                    if abs(i - x) <= 1 and abs(j - y) <= 1:
                        # dsu.union(8 * x + y, 8 * i + j)
                        if i == x and j == y:
                            continue
                        danger[i][j] = True
                        
        

        def moveDiag(x, y, danger, chess):
            r = range(8)
            for d in r:
                if x + d not in r or y + d not in r:
                    break
                # dsu.union(8 * x + y, 8 * (x + d) + y + d)
                if d == 0:
                    continue
                danger[x + d][y + d] = True
                ch = chess[x + d][y + d]
                if ch not in ".k":
                    break
            for d in r:
                if x + d not in r or y - d not in r:
                    break
                # dsu.union(8 * x + y, 8 * (x + d) + y - d)
                if d == 0:
                    continue
                danger[x + d][y - d] = True
                ch = chess[x + d][y - d]
                if ch not in ".k":
                    break
            for d in r:
                if x - d not in r or y + d not in r:
                    break
                # dsu.union(8 * x + y, 8 * (x - d) + y + d)
                if d == 0:
                    continue
                danger[x - d][y + d] = True
                ch = chess[x - d][y + d]
                if ch not in ".k":
                    break
            for d in r:
                if x - d not in r or y - d not in r:
                    break
                # dsu.union(8 * x + y, 8 * (x - d) + y - d)
                if d == 0:
                    continue
                danger[x - d][y - d] = True
                ch = chess[x - d][y - d]
                if ch not in ".k":
                    break

        
        def moveHorVer(x, y, danger, chess):
            r = range(8)
            for d in r:
                if x + d not in r:
                    break
                # dsu.union(8 * x + y, 8 * (x + d) + y)
                if d == 0:
                    continue
                danger[x + d][y] = True
                ch = chess[x + d][y]
                if ch not in ".k":
                    break
            for d in r:
                if x - d not in r:
                    break
                # dsu.union(8 * x + y, 8 * (x - d) + y)
                if d == 0:
                    continue
                danger[x - d][y] = True
                ch = chess[x - d][y]
                if ch not in ".k":
                    break
            for d in r:
                if y + d not in r:
                    break
                # dsu.union(8 * x + y, 8 * x + y + d)
                if d == 0:
                    continue
                danger[x][y + d] = True
                ch = chess[x][y + d]
                if ch not in ".k":
                    break
            for d in r:
                if y - d not in r:
                    break
                # dsu.union(8 * x + y, 8 * x + y - d)
                if d == 0:
                    continue
                danger[x][y - d] = True
                ch = chess[x][y - d]
                if ch not in ".k":
                    break

        for x, y in queen:
            moveDiag(x, y, danger, chess)
            moveHorVer(x, y, danger, chess)
        
        for x, y in rook:
            moveHorVer(x, y, danger, chess)
        
        for x, y in bishop:
            moveDiag(x, y, danger, chess)
        
        for x, y in knight:
            for i in range(8):
                for j in range(8):
                    if i == x and j == y:
                        # dsu.union(8 * x + y, 8 * i + j)
                        # danger[i][j] = True
                        continue
                    if abs(i - x) + abs(j - y) == 3 and abs(i - x) * abs(j - y) == 2:
                        # dsu.union(8 * x + y, 8 * i + j)
                        danger[i][j] = True
        
        


        k = 8 * myking[0] + myking[1]
        # incheck = dsu.set_size(k) >= 1
        incheck = danger[myking[0]][myking[1]]


        dx = [1, 1, 1, 0, 0, -1, -1, -1]
        dy = [1, 0, -1, 1, -1, 1, 0, -1]

        canmove = False
        for ii in range(8):
            x, y = myking[0] + dx[ii], myking[1] + dy[ii]
            if 0 <= x < 8 and 0 <= y < 8:
                i, j = x, y
                # if dsu.set_size(8 * i + j) == 1:
                if not danger[i][j]:
                    canmove = True
                    # print(i, j)
                    break
        
        # print(incheck, canmove)

        # for row in danger:
        #     print(*[int(x) for x in row])

        if incheck:
            if canmove:
                print("CHECK")
            else:
                print("CHECKMATE")
        else:
            if canmove:
                print("SAFE")
            else:
                print("SAFE")


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
