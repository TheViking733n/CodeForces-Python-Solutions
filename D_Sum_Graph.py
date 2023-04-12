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

def query(a, b):
    print("?", a, b, flush=1)
    return int(input())

def main():
    TestCases = 1
    TestCases = int(input())

    # def transform(arr):
    #     n = len(arr)
    #     ans = []
    #     for i in range(1, n, 2):
    #         ans.append(arr[i])
    #     a2 = []
    #     for i in range(0, n, 2):
    #         a2.append(arr[i])
    #     ans.extend(a2[::-1])

    #     for i in range(n): ans[i] -= 1

    #     ind = [0] * n
    #     for i in range(n): ind[ans[i]] = i + 1

    #     return ind
    
    for _ in range(TestCases):
        n = int(input())

        print("+", n + 1, flush=1); input()
        print("+", n, flush=1); input()

        d = query(1, 2)
        dis1, dis2 = [-1] * (n + 1), [-1] * (n + 1)
        dis1[2] = dis2[1] = d
        for i in range(3, n + 1):
            dis1[i] = query(1, i)
            dis2[i] = query(2, i)

        arr = []
        v1, v2 = n, 1
        for i in range(n):
            if i & 1:
                arr.append(v2)
                v2 += 1
            else:
                arr.append(v1)
                v1 -= 1
        # print(arr)
        ind = [0] * (n + 1)   # Inverse of arr
        for i in range(n):
            ind[arr[i]] = i
        
        def getDistance(u, v):
            return abs(ind[u] - ind[v])
        
        dist = [[set() for i in range(n)] for i in range(n+1)]

        for i in range(n):
            cur = arr[i]
            for j in range(n):
                i1, i2 = i - j, i + j
                if 0 <= i1 < n:
                    dist[cur][j].add(arr[i1])
                if 0 <= i2 < n:
                    dist[cur][j].add(arr[i2])
        
        # for row in dist:
        #     print(*row)

        mx1, mx2 = max(dis1), max(dis2)
        # mx1, mx2, d = 3, 5, 2
        p1 = [arr[mx1], arr[n - mx1 - 1]]
        p2 = [arr[mx2], arr[n - mx2 - 1]]
        # print(p1, p2)
        p1p2 = []
        for p1_ in p1:
            for p2_ in p2:
                if p1_ != p2_ and getDistance(p1_, p2_) == d:
                    p1p2.append((p1_, p2_))
        # print(p1p2)
        p1p2 = list(set(p1p2))

        ans = []
        for p1, p2 in p1p2:
            perm = [-1] * (n + 1)
            perm[1], perm[2] = p1, p2
            try:
                for pi in range(3, n + 1):
                    val = list(dist[p1][dis1[pi]].intersection(dist[p2][dis2[pi]]))[0]
                    perm[pi] = val
                ans.append(perm[1:])
            except:
                pass
        
        # print(ans)
        if len(ans) == 1:
            # ans.extend(ans[0][::-1])
            ans *= 2
        print("!", *ans[0], *ans[1], flush=1)
        input()
                

                    





























        

        # d = query(1, n)
        # dis1 = [0] * n
        # disN = [0] * n
        # dis1[-1] = disN[-1] = d
        # for i in range(2, n):
        #     dis1[i] = query(1, i)
        #     disN[i] = query(n, i)        


        # ans = []
        # for posN in range(n):
        #     ans1 = [-1] * n
        #     ans2 = [-1] * n
        #     ans1[posN] = ans2[posN] = n
        #     for i in range(2, n):
        #         try:
        #             pos1 = posN + d
        #             ans1[pos1] = 1
        #             if disN[i] + dis1[i] == d:
        #                 ans1[posN + disN[i]] = i
        #             elif disN[i] > dis1[i]:
        #                 ans1[posN + disN[i]] = i
        #             else:
        #                 ans1[max(0, posN - disN[i])] = i
        #         except:
        #             pass
        #         try:
        #             pos1 = posN - d
        #             if pos1 < 0: continue
        #             ans2[pos1] = 1
        #             if disN[i] + dis1[i] == d:
        #                 ans2[pos1 + dis1[i]] = i
        #             elif dis1[i] > disN[i]:
        #                 ans2[pos1 + dis1[i]] = i
        #             else:
        #                 ans2[max(0, pos1 - dis1[i])] = i
        #         except:
        #             pass
            
        #     if -1 not in ans1:
        #         ans.append(ans1)
        #     if -1 not in ans2:
        #         ans.append(ans2)
        
        # if len(ans) == 1:
        #     ans *= 2
        
        # ans = [transform(i) for i in ans]
        # # print(ans)
        # print('!', *ans[0], *ans[1], flush=1)




        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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

# class Wrapper(int):
#     def __init__(self, x):
#         int.__init__(x)
#     def __hash__(self):
#         return super(Wrapper, self).__hash__() ^ R
# Int = lambda x:Wrapper(int(x))        

# class myDict():
#     def __init__(self,func=int):
#         # self.RANDOM = randint(0,1<<32)
#         self.RANDOM = R
#         self.default=func
#         self.dict={}
#     def __getitem__(self,key):
#         myKey=self.RANDOM^key
#         if myKey not in self.dict:
#             self.dict[myKey]=self.default()
#         return self.dict[myKey]
#     def __setitem__(self,key,item):
#         myKey=self.RANDOM^key
#         self.dict[myKey]=item
#     def __contains__(self,key):
#         myKey=self.RANDOM^key
#         return myKey in self.dict
#     def __delitem__(self,key):
#         myKey=self.RANDOM^key
#         del self.dict[myKey]
#     def keys(self):
#         return [self.RANDOM^i for i in self.dict]


# # =============================== Region Fastio ===============================
# if not os.path.isdir('C:/users/acer'):
#     BUFSIZE = 8192
    
    
#     class FastIO(IOBase):
#         newlines = 0
    
#         def __init__(self, file):
#             self._fd = file.fileno()
#             self.buffer = BytesIO()
#             self.writable = "x" in file.mode or "r" not in file.mode
#             self.write = self.buffer.write if self.writable else None
    
#         def read(self):
#             while True:
#                 b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
#                 if not b:
#                     break
#                 ptr = self.buffer.tell()
#                 self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
#             self.newlines = 0
#             return self.buffer.read()
    
#         def readline(self):
#             while self.newlines == 0:
#                 b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
#                 self.newlines = b.count(b"\n") + (not b)
#                 ptr = self.buffer.tell()
#                 self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
#             self.newlines -= 1
#             return self.buffer.readline()
    
#         def flush(self):
#             if self.writable:
#                 os.write(self._fd, self.buffer.getvalue())
#                 self.buffer.truncate(0), self.buffer.seek(0)
    
    
#     class IOWrapper(IOBase):
#         def __init__(self, file):
#             self.buffer = FastIO(file)
#             self.flush = self.buffer.flush
#             self.writable = self.buffer.writable
#             self.write = lambda s: self.buffer.write(s.encode("ascii"))
#             self.read = lambda: self.buffer.read().decode("ascii")
#             self.readline = lambda: self.buffer.readline().decode("ascii")
    
    
#     def print(*args, **kwargs):
#         """Prints the values to a stream, or to sys.stdout by default."""
#         sep, file = kwargs.pop("sep", " "), kwargs.pop("file", sys.stdout)
#         at_start = True
#         for x in args:
#             if not at_start:
#                 file.write(sep)
#             file.write(str(x))
#             at_start = False
#         file.write(kwargs.pop("end", "\n"))
#         if kwargs.pop("flush", False):
#             file.flush()
    
    
#     if sys.version_info[0] < 3:
#         sys.stdin, sys.stdout = FastIO(sys.stdin), FastIO(sys.stdout)
#     else:
#         sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
    
#     input = lambda: sys.stdin.readline().rstrip("\r\n")

# =============================== Endregion ===============================

if __name__ == "__main__":
    #read()
    main()
    #dmain()
