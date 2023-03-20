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

def all_eq(cc):
    for i in range(len(cc)-1):
        if cc[i][1] != cc[i+1][1]:
            return False
    return True

def main():
    TestCases = 1
    TestCases = int(input())

    for _ in range(TestCases):
        n = int(input())
        arr = [int(i) for i in input().split()]

        freq_lst = Counter(arr).most_common()
        freq_lst.reverse()
        freq_arr = [i[1] for i in freq_lst]
        total = n    # Sum of all frequencies will be equal to no. of elements

        ans = INF
        for i in range(len(freq_arr)):
            cur = freq_arr[i]
            sm = total - cur*(len(freq_arr) - i)
            ans = min(ans, sm)
        print(ans)

        




















        # # --------------------------
        # # Working Code Method 1 Starts

        # cnt = Counter(arr)
        # cc = cnt.most_common()
        # cc.reverse()
        # # print(cc)
        
        # if all_eq(cc):
        #     print(0)
        #     continue

        # arr = [i[1] for i in cc]
        # # print(arr)
        # n = len(arr)
        # total = sum(arr)
        # ps = [0]
        # for i in range(n):
        #     ps.append(ps[-1]+arr[i])
        
        # unique = list(set(arr))
        # cnt = Counter(arr)
        # ps2 = {}
        # sm = 0
        # for i in unique:
        #     ps2[i] = sm
        #     sm += cnt[i]*i


        # ans = INF

        # # print(unique)
        # # print(ps2)

        # freq = {}
        # sm = 0
        # for i in range(len(unique)-1, -1, -1):
        #     val = unique[i]
        #     sm += cnt[val]
        #     freq[val] = sm
        # # print(freq)


        # for i in range(len(unique)):
        #     cur = unique[i]
        #     sm1 = ps2[cur]
        #     sm2 = (total-sm1) - freq[cur]*cur
        #     ans = min(sm1+sm2, ans)
        #     # print(cur, sm1, sm2)
        
        # print(ans)


        # # Working Code Method 1 Ends
        # # --------------------------
















        # for i in range(n):
        #     sm = ps[i+1]
        #     sm2 = (total-sm) - (n-i-1)*arr[i]
        #     print(i, sm, sm2)
        #     ans = min(ans, sm+sm2)
        # print(ans)

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # freq_arr = [i[1] for i in cc]
        # freq_freq_cnt = Counter(freq_arr)
        # freq_freq = freq_freq_cnt.most_common()

        # ff = [i[1] for i in freq_freq]
        # ff.reverse()

        # # print(freq_arr)
        # # print(ff)

        # unique_freq = list(set(freq_arr))

        # ans = INF

        # for i in range(len(unique_freq)-1):
        #     cur = unique_freq[i]
        #     sm = 0
        #     for j in range(i+1, len(unique_freq)):
        #         sm += (unique_freq[j]-unique_freq[i+1])*freq_freq_cnt[unique_freq[j]]
        #     for j in range(i+1):
        #         sm += unique_freq[j]*freq_freq_cnt[unique_freq[j]]
        
        #     ans = min(ans, sm)
        #     # print(sm)
        
        # print(ans)


        
        
        
        
        
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

