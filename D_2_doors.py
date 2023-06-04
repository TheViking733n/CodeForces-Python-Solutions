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

def scc(graph):
    """
    Finds what strongly connected components each node
    is a part of in a directed graph,
    it also finds a weak topological ordering of the nodes
    """
    n = len(graph)
    comp = [-1] * n
    top_order = []

    Q = []
    stack = []
    new_node = None
    for root in range(n):
        if comp[root] >= 0:
            continue

        # Do a dfs while keeping track of depth
        Q.append(root)
        root_depth = len(top_order)
        while Q:
            node = Q.pop()
            if node >= 0:
                if comp[node] >= 0:
                    continue
                # First time

                # Index the node
                comp[node] = len(top_order) + len(stack)
                stack.append(node)

                # Do a dfs
                Q.append(~node)
                Q += graph[node]
            else:
                # Second time
                node = ~node

                # calc low link
                low = index = comp[node]
                for nei in graph[node]:
                    if root_depth <= comp[nei]:
                        low = min(low, comp[nei])

                # low link same as index, so create SCC
                if low == index:
                    while new_node != node:
                        new_node = stack.pop()
                        comp[new_node] = index
                        top_order.append(new_node)
                else:
                    comp[node] = low

    top_order.reverse()
    return comp, top_order

 
class TwoSat:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(2 * n)]
 
    def _imply(self, x, y):
        self.graph[x].append(y if y >= 0 else 2 * self.n + y)
 
    def either(self, x, y):
        """either x or y must be True"""
        self._imply(~x, y)
        self._imply(~y, x)
 
    def set(self, x):
        """x must be True"""
        self._imply(~x, x)
 
    def solve(self):
        comp, top_order = scc(self.graph)
        for x in range(self.n):
            if comp[x] == comp[~x]:
                return False, None

        self.values = [None] * self.n
        for x in reversed(top_order):
            y = x if x < self.n else (2 * self.n - 1 - x)
            if self.values[y] is None:
                self.values[y] = x < self.n
        return True, self.values


# def solve(n, edges, zeroes, ones):
#     tree = [[] for _ in range(n)]
#     ans = [-1] * n
#     for pa, ch in edges:
#         tree[ch].append(pa)
#         ans[pa] = ans[ch] = 1
#     for u in zeroes: ans[u] = 0
#     for u in ones: ans[u] = 1
#     for i in range(n): ans[i] = max(ans[i], 0)
#     # For every child in tree,
#     # if any of its parent is 0, then it must be 1
#     # if all its parent are 1 or it has no parent, then it will be 0
#     for i in range(n):
#         if not ans[i] or i in ones: continue
#         zeroParFound = False
#         for pa in tree[i]:
#             if ans[pa] == 0:
#                 zeroParFound = True
#                 break
#         if not zeroParFound:
#             ans[i] = 0
#     return ans

def solve(n, edges, zeroes, ones):
    sat = TwoSat(n)
    for x, y in edges: sat.either(x, y)
    for x in zeroes: sat.set(~x)
    for x in ones: sat.set(x)
    return sat.solve()[1]

def main():
    TestCases = 1
    
    for _ in range(TestCases):
        n, q = [int(i) for i in input().split()]
        queries = []
        for _ in range(q):
            u, v, w = [int(i) - 1 for i in input().split()]
            queries.append((min(u, v), max(u, v), w + 1))
        ans = [0] * n
        for bit in range(30):
            mask = 1 << bit
            sat = TwoSat(n)
            for u, v, w in queries:
                if w & mask:
                    if u == v: sat.set(u)
                    else: sat.either(u, v)
                else:
                    sat.set(~u)
                    if u != v: sat.set(~v)
            curans = sat.solve()[1]
            for i in range(n):
                ans[i] |= curans[i] << bit
        print(*ans)

        # for bit in range(30):
        #     mask = 1 << bit
        #     edges, zeroes, ones = [], set(), set()
        #     for u, v, w in queries:
        #         if w & mask:
        #             if u == v: ones.add(u)
        #             else: edges.append((u, v))
        #         else:
        #             zeroes.add(u)
        #             zeroes.add(v)
        #     curans = solve(n, edges, zeroes, ones)
        #     for i in range(n):
        #         ans[i] |= curans[i] << bit
        # print(*ans)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
