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
oo = 9223372036854775807
PI = 3.141592653589793
R = randrange(2, 1 << 32)
# R = 0          # Enable this for debugging of dict keys in myDict

# ========================= Main ==========================

def encode(x, y): return x << 20 | y
def decode(z): return z >> 20, z & 0xfffff


class RangeQuery:
    def __init__(self, data, func=min):
        self.func = func
        self._data = _data = [list(data)]
        i, n = 1, len(_data[0])
        while 2 * i <= n:
            prev = _data[-1]
            _data.append([func(prev[j], prev[j + i]) for j in range(n - 2 * i + 1)])
            i <<= 1

    def query(self, start, stop):
        """func of data[start, stop)"""
        depth = (stop - start).bit_length() - 1
        return self.func(self._data[depth][start], self._data[depth][stop - (1 << depth)])

    def __getitem__(self, idx):
        return self._data[0][idx]




def build(node, lo, hi):
    if hi == lo:
        tree[node].append(arr[lo-1])
        return

    mid = (lo + hi) // 2
    build(2 * node, lo, mid)
    build(2 * node + 1, mid + 1, hi)

    tree[node] = sorted(tree[2 * node] + tree[2 * node + 1])

def _query(node, lo, hi, x, y, k):
    if lo > y or hi < x:
        return 0
    if lo >= x and hi <= y:
        # return len(tree[node]) - bisect_right(tree[node], k)
        return bisect_left(tree[node], k)

    mid = (lo + hi) // 2

    return _query(2 * node, lo, mid, x, y, k) + _query(2 * node + 1, mid + 1, hi, x, y, k)

def query(l, r, k): # returns no. of elements <= k in [l, r]
    r += 1
    l += 1
    if l > r:
        return 0
    if l == r:
        return int(arr[l-1] <= k)
    print(arr[l-1:r], [l-1, r-1], k)
    # return r - l + 1 - _query(1, 1, n, l, r, k)
    return _query(1, 1, n, l, r, k)

def isGood(sub): return sub.index(min(sub)) < sub.index(max(sub))
def brute(st, en):
    ans = 0
    a2 = arr[st:en+1]
    n = len(a2)
    for i in range(n):
        for j in range(i+1, n):
            sub = a2[i:j+1]
            if isGood(sub):
                subarr_brute.add(tuple(sub))
                ans += 1
    return ans

import functools

def monitor_results(func):
    @functools.wraps(func)
    def wrapper(*func_args, **func_kwargs):
        st, en = func_args
        print('calling ' + f'f({st}, {en})')
        retval = func(*func_args,**func_kwargs)
        correctval = brute(st, en)
        # print('function ' + func.__name__ + '() returns ' + repr(retval))
        print(f'f({st}, {en}) = {retval} | {arr[st:en+1]}')
        if retval != correctval:
            print(f'  => Wrong answer: expected {correctval}')
        return retval
    return wrapper

subarr_brute = set()
subarr_fast = set()

# @monitor_results
def f(st, en):
    # print(st, en, arr[st:en+1])
    if st >= en:
        # print(f'  => {st} {en}\t:', 0)
        return 0
    # if st + 1 == en:
        # print(f'  => {st} {en}\t:', int(arr[st] < arr[en]))
        # return int(arr[st] < arr[en])
    mn0, i1 = decode(rmn.query(st, en+1))
    mx0, i2 = decode(rmx.query(st, en+1))
    print(f'{i1=} {i2=}')
    ans = 0
    '''
    Case - I:
    0 1 2 3 4 5 6 7 8
        L     R    
    l            r
    l      r      
            l     r
    '''
    if i1 < i2:
        left = i1 - st + 1
        mid = i2 - i1 - 1
        right = en - i2 + 1
        ans += left * right
        # for i in range(st, i1 + 1):
        #     for j in range(i2, en + 1):
        #         i11, j11 = sorted([i, j]); sub = arr[i11:j11+1]
        #         if not isGood(sub): print('Bad1 ->', sub)
        #         else: subarr_fast.add(tuple(sub))
        mx = -oo; mn = oo
        for i in range(i1 + 1, i2):
            mx = max(mx, arr[i])
            # Find leftmost index in [st, i1] such that max(arr[idx..i1]) < mx
            low, high = st, i1; idx = i1
            while low <= high:
                mid = low + high >> 1
                if (rmx.query(mid, i1+1)>>20) < mx:
                    high = mid - 1
                    idx = mid
                else:
                    low = mid + 1
            ans += i1 - idx + 1
            # for j in range(idx, i1+1):
            #     i11, j11 = sorted([i, j]); sub = arr[i11:j11+1]
            #     if not isGood(sub): print('Bad2 ->', sub)
            #     else: subarr_fast.add(tuple(sub))

        for i in range(i2 - 1, i1, -1):
            mn = min(mn, arr[i])
            # Find rightmost index in [i2, en] such that min(arr[i2..idx]) > mn
            low, high = i2, en; idx = i2
            while low <= high:
                mid = low + high >> 1
                if (rmn.query(i2, mid+1)>>20) > mn:
                    low = mid + 1
                    idx = mid
                else:
                    high = mid - 1
            ans += idx - i2 + 1
            # for j in range(i2, idx+1):
            #     i11, j11 = sorted([i, j]); sub = arr[i11:j11+1]
            #     if not isGood(sub): print('Bad3 ->', sub)
            #     else: subarr_fast.add(tuple(sub))

        # ans += left * mid
        # ans += mid * right

    
        '''
        Case - II:
        0 1 2 3 4 5 6 7 8
            R     L    
        l           r       -> No sol
        l     r
                l     r
            
        '''

    elif i1 > i2:
        i1, i2 = i2, i1
        # left = i1 - st
        # mid = i2 - i1
        # right = en - i2
        mn = oo; mx = -oo
        for i in range(i1-1, st-1, -1):
            mn = min(mn, arr[i])
            # Find rightmost index in [i1, i2-1] such that min(arr[i1..idx]) > mn
            low, high = i1, i2-1; idx = i1
            print(f'going to do binary search: {low=} {high=}')
            while low <= high:
                mid = low + high >> 1
                if (rmn.query(i1, mid+1)>>20) > mn:
                    low = mid + 1
                    idx = mid
                else:
                    high = mid - 1
            print(f'binary search done: {idx=}')
            ans += idx - i1 + 1
            # print(f'ans incremented by {idx - i1 + 1}')
            # for j in range(i1, idx+1):
            #     i11, j11 = sorted([i, j]); sub = arr[i11:j11+1]
            #     if not isGood(sub): print('Bad4 ->', sub, i, j, idx, idx - i1 + 1)
            #     else: subarr_fast.add(tuple(sub))

        for i in range(i2 + 1, en + 1):
            mx = max(mx, arr[i])
            # Find leftmost index in [i1+1, i2] such that max(arr[idx..i2]) < mx
            low, high = i1+1, i2; idx = i2
            while low <= high:
                mid = low + high >> 1
                if (rmx.query(mid, i2+1)>>20) < mx:
                    high = mid - 1
                    idx = mid
                else:
                    low = mid + 1
            ans += i2 - idx + 1
            # for j in range(idx, i2+1):
            #     i11, j11 = sorted([i, j]); sub = arr[i11:j11+1]
            #     if not isGood(sub): print('Bad5 ->', sub)
            #     else: subarr_fast.add(tuple(sub))


        # ans += left * mid
        # ans += mid * right

    # print(ans)
    ans += f(st, i1-1)
    ans += f(i1 + 1, i2 - 1)
    ans += f(i2+1, en)
    # print(f'  => {st} {en}\t:', ans)
    return ans








# def f(st, en):
#     if st >= en:
#         return 0
#     mid = st + en >> 1
#     ans = 0
#     for i in range(mid + 1, en + 1):
        


# def f(st, en):
#     print(st, en, arr[st:en+1])
#     if st >= en:
#         print(f'  => {st} {en}\t:', 0)
#         return 0
#     if st + 1 == en:
#         print(f'  => {st} {en}\t:', int(arr[st] < arr[en]))
#         return int(arr[st] < arr[en])
#     mn, i1 = decode(rmn.query(st, en+1))
#     mx, i2 = decode(rmx.query(st, en+1))
    
#     ans = 0
#     if i1 < i2:
#         left = i1 - st + 1
#         right = en - i2 + 1
#         ans += left * right
#         # print(left, right)
#         ans += left * (i2 - i1 - 1 - query(i1 + 1, i2 - 1, mn))
#         # print(left, right)
#         # print((i1 + 1, i2 - 1))
#         # print(mx, right, query(i1 + 1, i2 - 1, mx))
#         ans += right * (query(i1 + 1, i2 - 1, mx))
#     if i1 > i2:
#         i1, i2 = i2, i1
#         mid = i2 - i1
#         ans += mid * (query(st, i1 - 1, mx))
#         ans += mid * (en - i2 - query(i2 + 1, en, mn))
#     ans += f(st, i1 - 1)
#     ans += f(i1 + 1, i2 - 1)
#     ans += f(i2 + 1, en)
#     print(f'  => {st} {en}\t:', ans)
#     return ans
# print(f(0, n-1))
rmn = rmx = arr = n = tree = None

# [6, 2, 4, 1, 7, 3, 8, 5, 0]

def main():
    global rmn, rmx, arr, arr, n, tree
    # n = int(input())
    # arr = [int(i) - 1 for i in input().split()]
    n = 4 * 10 ** 3; arr = list(range(n))
    # print(arr[:n])
    a2 = [encode(arr[i], i) for i in range(n)]
    rmn = RangeQuery(a2, min)
    rmx = RangeQuery(a2, max)

    # tree = [[] for _ in range(n * (n.bit_length()))]
    # build(1, 1, n)
    # print(tree)

    # print(query(2, 5, 2))


    print(f(0, n-1))

    # print(subarr_brute - subarr_fast)
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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

