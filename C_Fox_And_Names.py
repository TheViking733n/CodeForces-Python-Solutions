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
from collections import deque, Counter, OrderedDict
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

def check_for_cycle(node, visited, vis, graph):
    visited[node] = True
    vis[node] = True
    for ch in graph[node]:
        if not visited[ch]:
            if check_for_cycle(ch, visited, vis, graph):
                return True
        elif vis[ch]:
            return True
    vis[node] = False
    return False


def dfs(node, visited, graph, ans):
    visited[node] = True
    for ch in graph[node]:
        if not visited[ch]:
            dfs(ch, visited, graph, ans)
    ans.append(node)


def main():
    TestCases = 1

    for _ in range(TestCases):
        n = int(input())        
        # arr = [input() for i in range(n)]
        pairs = set()
        possible = True
        prev = input()
        for i in range(n-1):
            a, b = prev, input()
            if a == b:
                continue
            if a.startswith(b):
                possible = False
                break
        
            for j in range(min(len(a), len(b))):
                if a[j] != b[j]:
                    pairs.add((a[j], b[j]))
                    break
            prev = b
            
        if not possible:
            print("Impossible")
            continue
        
        pairs = list(pairs)
        # print(pairs)

        graph = defaultdict(list)
        for u, v in pairs:
            graph[u].append(v)
        

        # First checking for cycle in the graph
        visited = defaultdict(bool)
        vis = defaultdict(bool)
        isCyclic = False
        for ch in abc:
            if not visited[ch] and check_for_cycle(ch, visited, vis, graph):
                isCyclic = True
                break
        
        if isCyclic:
            print("Impossible")
            continue



        # Topological Sort
        ans = []

        visited = defaultdict(bool)
        for ch in abc:
            if not visited[ch]:
                dfs(ch, visited, graph, ans)
        
        ans.reverse()
        print(*ans, sep='')

        
        
        
        
        
        
        
        
        
        
        
        
        
        # graph = defaultdict(list)
        # roots = set(abc)
        # for u, v in pairs:
        #     graph[v].append(u)
        #     if u in roots:
        #         roots.remove(u)
        
        # # print(dict(graph))

        # roots = list(roots)
        # if not roots:
        #     print("Impossible")
        #     continue

        # graph[0] = roots

        # # print(dict(graph))

        # # Check for cycle in the graph
        # visited = defaultdict(bool)
        
        # # for ch in abc:
        # #     if not visited[ch]:
        # #         iscyclic = dfs(ch, visited, graph)
        # #         if iscyclic:
        # #             break
        # print(dfs(0, visited, graph))
        # iscyclic = len(visited) != 27
        # # print(iscyclic)
        # # print(len(visited))

        # if iscyclic:
        #     print("Impossible")
        #     continue

        # value = defaultdict(int)

        # q = deque([0])
        # while q:
        #     cur = q.popleft()
        #     v = value[cur]
        #     for ch in graph[cur]:
        #         # value[ch] = max(value[ch], v + 1)
        #         if value[ch] <= v:
        #             value[ch] = v + 1    
        #             q.append(ch)
            
        # # print(dict(value))
        
        # a2 = [(v, k) for (k,v) in value.items() if k != 0]
        # a2.sort()
        # ans = [i[1] for i in a2]
        # ans.reverse()
        # print(*ans, sep='')
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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

