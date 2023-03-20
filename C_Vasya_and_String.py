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

def consecutive_ele_with_sum_less_than_k(arr, k):
    n = len(arr)
    out = []
    for i in range(n,0,-1):
        for j in range(0,n-i+1):
            sm = sum(arr[j:j+i]) 
            if sm<=k:
                out.append((j,j+i,sm))
        if out:
            break
    return out

def main():
    TestCases = 1
    # TestCases = int(input())

    for _ in range(TestCases):
        n,k = [int(i) for i in input().split()]
        # n = int(input())
        # arr = [int(i) for i in input().split()]
        s = input()

        arr = [ch for ch in s]

        a=arr.count('a')
        b=arr.count('b')
        low=1
        ps=[0]
        ans=0
        for i in range(n):
            if arr[i]=='a':
                ps.append(1+ps[-1])
            else:
                ps.append(ps[-1])
        
        print(ps)
        
        high=n
        while low<=high:
            mid=(low+high)//2
            valid=False
            for i in range(n-mid+1):
                start=i
                end=i+mid-1
                aCount=ps[end+1]-ps[start]
                bCount=mid-aCount
                if min(aCount,bCount)<=k:
                    valid=True
                    break
            if valid:
                low=mid+1
                ans=max(ans,mid)
            else:
                high=mid-1
        print(ans)









































        # if n==1:
        #     print(1)
        #     continue

        # # i, j = 0, 1

        # # while j<=n:
        # #     subseq = 


        # if n==k:
        #     print(n)
        #     continue
        
        # i = 1
        # c = [1]
        # while i<n:
        #     if s[i]==s[i-1]:
        #         c[-1]+=1
        #     else:
        #         c.append(1)
        #     i+=1

        # # print(c)

        # ln = len(c)
        # sm1 = sum(c[0::2])
        # sm2 = sum(c[1::2])
        # sm = sum(c)

        # i,j=0,ln-1
        # while i<=j:
        #     # ans1 = (sm2 if i&1 else sm1) if sm1<k else -1
        #     # ans2 = (sm1 if j&1 else sm1) if sm2<k else -1
        #     ans1 = sm if sm1<=k else -1
        #     ans2 = sm if sm2<=k else -1
        #     ans = max(ans1,ans2)
        #     if ans!=-1:
        #         print(ans)
        #         break
        #     if c[i]>=c[j]:
        #         if j&1:
        #             sm2-=c[j]
        #         else:
        #             sm1-=c[j]
        #         sm-=c[j]
        #         j-=1
        #     else:
        #         if i&1:
        #             sm2-=c[i]
        #         else:
        #             sm1-=c[i]
        #         sm-=c[i]
        #         i+=1






        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        



        # if len(c)==1:
        #     print(n)
        #     continue
        
        
        # ans = max(c)
        # smfs = [[0,0,0]]  # commutative sum first second nested list
        
        # for i in range(len(c)):
        #     # print(smfs[-1])
        #     x = smfs[-1][0] + c[i]
        #     y = smfs[-1][1] + c[i]*(1-i&1)
        #     z = smfs[-1][2] + c[i]*(i&1)
        #     smfs.append([x,y,z])
        # # print(smfs[-1])

        # ln = len(smfs)
        # for i in range(ln):
        #     for j in range(i+1,ln):
        #         ss = smfs[j][0]-smfs[i][0]
        #         aa = smfs[j][1]-smfs[i][1]
        #         bb = smfs[j][2]-smfs[i][2]
                
        #         if min(aa,bb)<=k:
        #             ans = max(ans, ss)



        # print(ans)











        # first = c[0::2]
        # second = c[1::2]

        # out = consecutive_ele_with_sum_less_than_k(first, k)

        # if not out:
        #     ans1 = max(second)

        # else:
        #     ans1 = 0
        #     for i1,i2,sm in out:
        #         x = second[i1-1:i2]
        #         ans1 = max(ans1, sm + sum(x if x else [0]))


        # out = consecutive_ele_with_sum_less_than_k(second, k)

        # if not out:
        #     ans2 = max(first)

        # else:
        #     ans2 = 0
        #     for i1,i2,sm in out:
        #         x = first[i1-1:i2]
        #         ans2 = max(ans2, sm + sum(x if x else [0]))


        # print(max(ans1, ans2))

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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

