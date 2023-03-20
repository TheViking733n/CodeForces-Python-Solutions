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
        a,b,c,d = [int(i) for i in input().split()]
        s = input()
        n = len(s)
        
        x = s.count('A')
        y = s.count('B')

        if not (a+c+d==x and b+c+d==y):
            print("NO")
            continue
        


        splited = [[s[0]]]
        for i in range(1, n):
            if s[i] != s[i-1]:
                splited[-1].append(s[i])
            else:
                splited.append([s[i]])
        
        # print(*["".join(x) for x in splited], sep='\n', end='\n\n')

        abab = []
        baba = []
        # abab = baba = 0
        odds = 0
        m = len(splited)
        for i in range(m):
            ln = len(splited[i])
            if ln&1:
                ln -= 1
                odds += ln//2
            
            elif splited[i][0] == 'A':
                abab.append(ln//2) # Length must be even
                # abab += ln//2
            
            else:
                baba.append(ln//2) # Length must be even
                # baba += ln//2
        

        # print(abab)
        # print(baba)
        # print(odds)

        abab.sort()
        baba.sort()

        for i in range(len(abab)):
            if c <= 0:
                break
            mn = min(c, abab[i])
            c -= mn
            abab[i] -= mn
        
        for i in range(len(baba)):
            if d <= 0:
                break
            mn = min(d, baba[i])
            d -= mn
            baba[i] -= mn

        if abab and abab[-1] > 0:
            # It means c is finished.
            # So, we can use d to finish the remaining.
            for i in range(len(abab)):
                if abab[i] == 0:
                    continue
                if d <= 0:
                    break
                abab[i] -= 1
                mn = min(d, abab[i])
                d -= mn
                abab[i] -= mn
        
        if baba and baba[-1] > 0:
            # It means d is finished.
            # So, we can use c to finish the remaining.
            for i in range(len(baba)):
                if baba[i] == 0:
                    continue
                if c <= 0:
                    break
                baba[i] -= 1
                mn = min(c, baba[i])
                c -= mn
                baba[i] -= mn
        
        if c > 0:
            mn = min(odds, c)
            c -= mn
            odds -= mn
        
        if d > 0:
            mn = min(odds, d)
            d -= mn
            odds -= mn
        
        if c > 0 or d > 0:
            print("NO")
        else:
            print("YES")

        



                



































        # ab = i = 0
        # while i<n:
        #     if s[i:i+2] == "AB":
        #         ab += 1
        #         i += 2
        #     else:
        #         i += 1
        
        # ba = i = 0
        # while i<n:
        #     if s[i:i+2] == "BA":
        #         ba += 1
        #         i += 2
        #     else:
        #         i += 1
        
        # aba = i = 0
        # while i<n:
        #     if s[i:i+3] == "ABA":
        #         aba += 1
        #         i += 3
        #     else:
        #         i += 1
        
        # bab = i = 0
        # while i<n:
        #     if s[i:i+3] == "BAB":
        #         bab += 1
        #         i += 3
        #     else:
        #         i += 1
        
        # print(ab,ba,aba,bab)







        # c1 = d1 = i = 0
        # while i<n:
        #     if c1<=c and s[i:i+2] == "AB":
        #         c1+=1
        #         i+=2
        #     elif d1<=d and s[i:i+2] == "BA":
        #         d1+=1
        #         i+=2
        #     else:
        #         i+=1
        
        # if c1>=c and d1>=d:
        #     print("YES")
        # else:
        #     print("NO")





        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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

