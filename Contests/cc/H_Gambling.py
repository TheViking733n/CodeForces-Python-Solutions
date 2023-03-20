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



def main():
    TestCases = 1
    TestCases = int(input())

    for _ in range(TestCases):
        # n,k = [int(i) for i in input().split()]
        n = int(input())
        arr = [int(i) for i in input().split()]
        # s = input()
        

        indarr = defaultdict(list)
        for i in range(n):
            indarr[arr[i]].append(i)
        
        ans = [0,0,0,0]

        # Using Kadane's Algorithm
        for num in indarr:
            a2 = [[1,indarr[num][0]]]
            for i in range(1,len(indarr[num])):
                diff = indarr[num][i] - indarr[num][i-1]
                if diff == 1:
                    a2.append([1,indarr[num][i]])
                else:
                    a2.append([1-diff,indarr[num][i-1]])
                    a2.append([1,indarr[num][i]])
            # print(indarr[num])
            # print(num,a2)


            mx = curmx = a2[0][0]
            prev_start = start = end = a2[0][1]
            for i in range(1, len(a2)):
                if a2[i][0] > curmx + a2[i][0]:
                    curmx = a2[i][0]
                    prev_start = a2[i][1]
                else:
                    curmx += a2[i][0]

                if curmx > mx:
                    mx = curmx
                    start = prev_start
                    end = a2[i][1]

            # print(mx+1, num, start+1, end+1)
            ans = max(ans, [mx+1, num, start+1, end+1])

        print(*ans[1:])


        # for num in indarr:
        #     mx = curmax = 1
        #     prev_l = l = r = indarr[num][0]
        #     print(num,indarr[num])
        #     for ii in range(1, len(indarr[num])):
        #         i = indarr[num][ii]
        #         val = 1 - 1 * (indarr[num][ii] - indarr[num][ii-1] - 1)
        #         # curmax = max(curmax, curmax + val)
        #         print(ii, val, curmax)
        #         if val > curmax + val:
        #             curmax = val
        #             prev_l = i
        #         else:
        #             curmax += val

        #         if curmax >= mx:
        #             mx = curmax
        #             l = prev_l
        #             r = i
        #     print(mx+1, num, l+1, r+1)
        #     ans.append([mx+1, num, l+1, r+1])

        # print(*max(ans)[1:])







        # My Method (TLE)
        # cnt = defaultdict(lambda:1)
        # ans = defaultdict(lambda:[0,0,0])
        # # print(cnt[2])
        # l = {}
        # r = {}
        # for i in range(n):
        #     num = arr[i]
        #     cnt[num] += 1
        #     if cnt[num] == 2:
        #         l[num] = i
        #     for k in cnt:
        #         if num!=k:
        #             cnt[k] = max(1, cnt[k] - 1)
        #     r[num] = i
        #     ans[num] = max(ans[num], [cnt[num],l[num]+1,r[num]+1])

        #     # print(dict(cnt),l,r)

        # # print(dict(ans))
        
        # vals = -1
        # for k in ans:
        #     if vals==-1:
        #         vals = [ans[k][0],k,ans[k][1],ans[k][2]]
        #         continue
        #     if ans[k][0]>vals[0]:
        #         vals = [ans[k][0],k,ans[k][1],ans[k][2]]
        
        # print(*vals[1:])
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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

