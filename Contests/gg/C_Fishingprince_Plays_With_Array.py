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

def possible(buf, val, m):
    print(buf, val, m)
    return 1

def main():
    TestCases = 1
    TestCases = int(input())


    for _ in range(TestCases):
        n,m = [int(i) for i in input().split()]
        # a = deque([int(i) for i in input().split()])
        a = [int(i) for i in input().split()]
        k = int(input())
        b = [int(i) for i in input().split()]
        # s = input()
        
        if sum(a)!=sum(b):
            print('No')
            continue



        a2 = deque([])
        for i in a:
            if i%m==0:
                m1 = m
                while i%(m1*m)==0:
                    m1 *= m
                num = i//m1
                freq = m1
                if a2 and a2[-1][0]==num:
                    a2[-1][1] += freq
                else:
                    a2.append([num, freq])
            else:
                num = i
                freq = 1
                if a2 and a2[-1][0]==num:
                    a2[-1][1] += freq
                else:
                    a2.append([num, freq])

        # print(list(a2))


        b2 = deque([])
        for i in b:
            if i%m==0:
                m1 = m
                while i%(m1*m)==0:
                    m1 *= m
                num = i//m1
                freq = m1
                if b2 and b2[-1][0]==num:
                    b2[-1][1] += freq
                else:
                    b2.append([num, freq])
            else:
                num = i
                freq = 1
                if b2 and b2[-1][0]==num:
                    b2[-1][1] += freq
                else:
                    b2.append([num, freq])

        # print(list(b2))

        print("Yes" if a2==b2 else "No")



















        # f = 1
        # buf = []
        # sm = 0
        # for i in range(len(b)):
        #     if not a2:
        #         f = 0
        #         break
        #     num, freq = a[0]
        #     s = num * freq
            
        #     while s+sm<=b[i]:
        #         num, freq = a[0]
        #         s = num * freq
        #         buf.append(a2.popleft())
        #         sm += s
            
        #     if sm<b[i]:




        #     if sm==b[i]:
        #         if freq
        #         a2.popleft()
        #         continue

        #     if sm<b[i]:


















        # buf = deque([])
        # i = j = sm = 0
        # while i<len(a) and j<len(b):
        #     print(i,j,buf)
        #     buf.append(a[i])
        #     sm += a[i]

        #     if sm<b[j]:
        #         i += 1
        #         continue

        #     if sm==b[j]:
        #         if possible(buf, b[j], m):
        #             buf = deque([])
        #             sm = 0
        #             j += 1
        #             continue
        #         else:
        #             break

            
        #     if sm>b[j]:
        #         break
        
        # if j==len(b):
        #     print('Yes')
        # else:
        #     print('No')
        





















        # f = 0
        # n = len(a)
        # i = 0; j = 0
        # while i<len(a) and j<k:
        #     print(list(a))
        #     if a[i]==b[j]:
        #         i+=1
        #         j+=1
        #         f = 0
        #         continue
            
        #     if a[i] > b[j] and a[i]%m==0:
        #         q = a[i]//m
        #         for x in range(i,i-m,-1):
        #             if x>=0:
        #                 a[x] = q
        #                 i = x
        #             else:
        #                 a.appendleft(q)
        #                 i = 0
        #         f = 1
        #         if a[i] != b[j] and f==2: break
        #         continue
        
        #     if a[i] < b[j]:
        #         cnt = 0
        #         for x in range(i,min(i+m,len(a))):
        #             if a[x]==a[i]:
        #                 cnt+=1
        #             else:
        #                 break
                
        #         if cnt==m:
        #             i = i + m -1
        #             a[i] = a[i]*m
        #             if a[i] != b[j] and f==1: break
        #             f = 2
        #             continue

        #     break

        # if j==k:
        #     print('Yes')
        # else:
        #     print("No")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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

