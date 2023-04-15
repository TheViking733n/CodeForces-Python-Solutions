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
def f(st, en, s, memo, msb):
    if st + 1 == en:
        yield s[st] != s[en]
    n = len(s)
    if memo[st<<msb|en] != -1:
        yield memo[st<<msb|en]
    # if st > en:
    #     return "", ""
    # print(st, en, end=' => ')

    # Alice chooses first
    # a1, b1 = f(st + 2, en, s)
    # a2, b2 = f(st + 1, en - 1, s)
    res1 = (yield f(st + 2, en, s, memo, msb)) or s[st] != s[st+1]
    res2 = (yield f(st + 1, en - 1, s, memo, msb)) or s[st] != s[en]
    ans1 = res1 and res2
    # a1 += s[st]; a2 += s[st]; b1 += s[st+1]; b2 += s[en]
    # a1 = s[st] + a1; a2 = s[st] + a2; b1 = s[st+1] + b1; b2 = s[en] + b2 
    # alice1, bob1 = (a1, b1) if b1 > a1 else (a2, b2)
    # if b1 == b2:
    #     alice1, bob1 = (a1, b1) if a1 > a2 else (a2, b2)
    # elif b1 < b2:
    #     alice1, bob1 = a1, b1
    # else:
    #     alice1, bob1 = a2, b2
    
    # Alice chooses last
    # a1, b1 = f(st + 1, en - 1, s)
    # a2, b2 = f(st, en - 2, s)
    res1 = (yield f(st, en - 2, s, memo, msb)) or s[en] != s[en-1]
    # res2 = yield f(st + 1, en - 1, s, memo, msb) or s[st] != s[en]
    ans2 = res1 and res2
    ans = ans1 or ans2
    memo[st<<msb|en] = ans
    yield ans
    # a1 += s[en]; a2 += s[en]; b1 += s[st]; b2 += s[en-1]
    # a1 = s[en] + a1; a2 = s[en] + a2; b1 = s[st] + b1; b2 = s[en-1] + b2 
    # alice2, bob2 = (a1, b1) if b1 > a1 else (a2, b2)
    # if b1 == b2:
    #     alice2, bob2 = (a1, b1) if a1 > a2 else (a2, b2)
    # elif b1 < b2:
    #     alice2, bob2 = a1, b1
    # else:
    #     alice2, bob2 = a2, b2
    
    # # x = (alice1, bob1) if alice1 < alice2 else (alice2, bob2)
    # if alice1 == alice2:
    #     x = (alice1, bob1) if bob1 > bob2 else (alice2, bob2)
    # if alice1 < alice2:
    #     x = alice1, bob1
    # else:
    #     x = alice2, bob2
    # print(x)
    # return x



def main():
    TestCases = 1
    TestCases = int(input())
    
    for _ in range(TestCases):
        s = input()
        n = len(s)
        i, j = 0, n - 1
        while i < j and s[i] == s[j]:
            i += 1
            j -= 1
        ans = "Draw"
        for k in range(i, j, 2):
            if s[k] != s[k+1]:
                ans = "Alice"
                break
        print(ans)

        # msb = len(s).bit_length()
        # memo = [-1] * (len(s) << msb)
        # print("Alice" if f(0, len(s) - 1, s, memo, msb) else "Draw")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
