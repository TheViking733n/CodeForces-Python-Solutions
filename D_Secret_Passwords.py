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

# C++ 31 ms code translated into python
# https://codeforces.com/problemset/submission/1263/136299666
z = 0
def main():
    global z
    f = [0] * 256

    def F(x):
        if f[ord(x)] != x:
            temp = F(f[ord(x)])
            f[ord(x)] = temp
            return temp
        else:
            return x

    def U(x, y):
        global z
        x = F(x)
        y = F(y)
        if x != y:
            f[ord(x)] = y
            z -= 1

    n = int(input())
    for i in range(n):
        s = input()
        for j in range(len(s)):
            if f[ord(s[j])] == 0:
                f[ord(s[j])] = s[j]
                z += 1
        for j in range(1, len(s)):
            U(s[j-1], s[j])
    print(z)























# def main():
#     n = int(input())
#     arr = [to_freq_list(input()) for i in range(n)]
#     graph = [[] for i in range(n+26)]
#     for i in range(n):
#         for j in range(26):
#             if arr[i][j]==1:
#                 graph[j+n].append(i)
#                 graph[i].append(j+n)
    
#     visited = [False] * (n + 26)
#     ans = 0
#     for i in range(n):
#         if not visited[i]:
#             ans += 1
#             dfs(i, visited, graph)

#     print(ans)

















# # ------------------------------------------------
# # Method 2

# def to_binary_num(alpha):
#     ans, i = 0, 1
#     # st = set(alpha)
#     # for ch in abc:
#     #     if ch in st:
#     #         ans += i
#     #     i <<= 1
#     # return ans
#     lst = to_freq_list(alpha)
#     for val in lst:
#         ans += val * i
#         i <<= 1
#     return ans

def to_freq_list(alpha):
    ans = [0] * 26
    sm = 0
    for ch in alpha:
        sm -= ans[abd[ch]]
        ans[abd[ch]] = min(ans[abd[ch]] + 1, 1)
        sm += ans[abd[ch]]
        if sm>=26:
            break
    return ans

# def op_OR(a, b):
#     return [a[i]|b[i] for i in range(26)]

# def main():
#     n = int(input())
#     arr = [to_binary_num(input()) for i in range(n)]


#     for i in range(26):
#         ind = -1
#         for j in range(n):
#             if arr[j] & (1 << i):
#                 if ind == -1:
#                     ind = j
#                 else:
#                     arr[ind] |= arr[j]
#                     arr[j] = 0

#     print(n-arr.count(0))







    # for i in range(26):
    #     arr2 = []
    #     other = [0] * 26
    #     for j in arr:
    #         if j[i]:
    #             other = op_OR(other, j)
    #         else:
    #             arr2.append(j)
    #         # print(arr2, other)
    #     if other != [0] * 26:
    #         arr2.append(other)
    
    #     arr = arr2
    # print(len(arr))














# # ------------------------------------------------
# # Method 1

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
def dfs(node, visited, graph):
    visited[node] = True
    for i in graph[node]:
        if not visited[i]:
            yield dfs(i, visited, graph)
    yield

# def main():
#     TestCases = 1

#     for _ in range(TestCases):
#         n = int(input())

#         arr = [set(input()) for i in range(n)]        

#         graph = [[] for i in range(n)]

#         for ch in abc:
#             last = -1
#             for i in range(n):
#                 if ch in arr[i]:
#                     if last != -1:
#                         graph[last].append(i)
#                         graph[i].append(last)
#                     last = i
            
        
#         # for i in range(n):
#         #     graph[i] = list(graph[i])

#         # print(graph)

#         visited = [False] * n
#         ans = 0
#         for i in range(n):
#             if not visited[i]:
#                 ans += 1
#                 dfs(i, visited, graph)

#         print(ans)



        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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

