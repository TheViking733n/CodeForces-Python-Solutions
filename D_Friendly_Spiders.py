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

def isPrimeMR(n):
    d = n - 1
    d = d // (d & -d)
    L = [2, 7, 61] if n < 1<<32 else [2, 3, 5, 7, 11, 13, 17] if n < 1<<48 else [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    # L = [2, 3, 5, 7, 11, 13, 17]
    if n in L:
        return 1
    for a in L:
        t = d
        y = pow(a, t, n)
        if y == 1: continue
        while y != n - 1:
            y = (y * y) % n
            if y == 1 or t == n - 1: return 0
            t <<= 1
    return 1
 
def findFactorRho(n):
    from math import gcd
    m = 1 << n.bit_length() // 8
    for c in range(1, 99):
        f = lambda x: (x * x + c) % n
        y, r, q, g = 2, 1, 1, 1
        while g == 1:
            x = y
            for i in range(r):
                y = f(y)
            k = 0
            while k < r and g == 1:
                ys = y
                for i in range(min(m, r - k)):
                    y = f(y)
                    q = q * abs(x - y) % n
                g = gcd(q, n)
                k += m
            r <<= 1
        if g == n:
            g = 1
            while g == 1:
                ys = f(ys)
                g = gcd(abs(x - ys), n)
        if g < n:
            if isPrimeMR(g): return g
            elif isPrimeMR(n // g): return n // g
            return findFactorRho(g)
 
def primeFactor(n):
    i = 2
    ret = {}
    rhoFlg = 0
    while i*i <= n:
        k = 0
        while n % i == 0:
            n //= i
            k += 1
        if k: ret[i] = k
        i += 1 + i % 2
        if i == 101 and n >= 2 ** 20:
            while n > 1:
                if isPrimeMR(n):
                    ret[n], n = 1, 1
                else:
                    rhoFlg = 1
                    j = findFactorRho(n)
                    k = 0
                    while n % j == 0:
                        n //= j
                        k += 1
                    ret[j] = k
 
    if n > 1: ret[n] = 1
    if rhoFlg: ret = {x: ret[x] for x in sorted(ret)}
    return list(ret.keys())

def memodict(f):
    """memoization decorator for a function taking a single argument"""
    class memodict(dict):
        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret
    return memodict().__getitem__
def pollard_rho(n):
    """returns a random factor of n"""
    if n & 1 == 0:
        return 2
    if n % 3 == 0:
        return 3
    s = ((n - 1) & (1 - n)).bit_length() - 1
    d = n >> s
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        p = pow(a, d, n)
        if p == 1 or p == n - 1 or a % n == 0:
            continue
        for _ in range(s):
            prev = p
            p = (p * p) % n
            if p == 1:
                return gcd(prev - 1, n)
            if p == n - 1:
                break
        else:
            for i in range(2, n):
                x, y = i, (i * i + 1) % n
                f = gcd(abs(x - y), n)
                while f == 1:
                    x, y = (x * x + 1) % n, (y * y + 1) % n
                    y = (y * y + 1) % n
                    f = gcd(abs(x - y), n)
                if f != n:
                    return f
    return n


@memodict
def prime_factors(n):
    """returns a Counter of the prime factorization of n"""
    if n <= 1:
        return Counter()
    f = pollard_rho(n)
    return [i for i in (Counter([n]) if f == n else prime_factors(f) + prime_factors(n // f))]


def distinct_factors(n):
    """returns a list of all distinct factors of n"""
    factors = [1]
    for p, exp in prime_factors(n).items():
        factors += [p**i * factor for factor in factors for i in range(1, exp + 1)]
    return factors


def all_factors(n):
    """returns a sorted list of all distinct factors of n"""
    small, large = [], []
    for i in range(1, int(n**0.5) + 1, 2 if n & 1 else 1):
        if not n % i:
            small.append(i)
            large.append(n // i)
    if small[-1] == large[-1]:
        large.pop()
    large.reverse()
    small.extend(large)
    return small



MAXN = int(3e5) + 10
 
# stores smallest prime factor for
# every number
spf = [0 for i in range(MAXN)]
 
# Calculating SPF (Smallest Prime Factor)
# for every number till MAXN.
# Time Complexity : O(nloglogn)
def sieve():
    spf[1] = 1
    for i in range(2, MAXN):
         
        # marking smallest prime factor
        # for every number to be itself.
        spf[i] = i
 
    # separately marking spf for
    # every even number as 2
    for i in range(4, MAXN, 2):
        spf[i] = 2
 
    for i in range(3, int(MAXN ** 0.5) + 1):
         
        # checking if i is prime
        if (spf[i] == i):
             
            # marking SPF for all numbers
            # divisible by i
            for j in range(i * i, MAXN, i):
                 
                # marking spf[j] if it is
                # not previously marked
                if (spf[j] == j):
                    spf[j] = i

def getFactorization(x):
    ret = list()
    while (x != 1):
        ret.append(spf[x])
        x = x // spf[x]
 
    return ret


def main():
    TestCases = 1
    # sieve()

    for _ in range(TestCases):
        n = int(input())
        arr = [int(i) for i in input().split()]
        u, v = [int(i)-1 for i in input().split()]

        if u == v:
            print(1, u + 1, sep = '\n')
            continue
        
        if gcd(arr[u], arr[v]) != 1:
            print(2)
            print(u + 1, v + 1)
            continue



        N = max(arr) + 1



        g = [set() for i in range(N)]
        dd = defaultdict(set)
        common = defaultdict(int)
        for i in range(n):
            pf = primeFactor(arr[i])
            for j in range(len(pf) - 1):
                g[pf[j]].add(pf[j + 1])
                g[pf[j + 1]].add(pf[j])
                for k in range(j + 1, len(pf)):
                    common[pf[j] * pf[k]] = i
                # dd[pf[j]].add(i)
            # if pf:
            #     dd[pf[-1]].add(i)
        
        dest = set(primeFactor(arr[v]))
        done = False
        # print(primeFactor(arr[u]))
        for source in primeFactor(arr[u]):
            q = deque([source])
            parent = [-1] * N
            vis = [0] * N
            vis[source] = True
            last = -1
            f = 1
            while q:
                x = q.popleft()
                if x in dest:
                    last = x
                    break
                for y in g[x]:
                    if not vis[y]:
                        vis[y] = True
                        parent[y] = x
                        q.append(y)
                
            if last == -1:
                continue

            path = []
            while last != -1:
                # path.append(dd[last][0] + 1)
                path.append(last)
                last = parent[last]
            
            # print(len(path))
            # print(*path[::-1])
            path.reverse()
            ans = [u+1]
            for i in range(len(path) - 1):
                x, y = path[i], path[i + 1]
                ans.append(common[x * y] + 1)
                # st = dd[x].intersection(dd[y])
                # ans.append(st.pop() + 1)
            ans.append(v + 1)
            ans2 = [ans[0]]
            for i in range(1, len(ans)):
                if ans[i] != ans[i - 1]:
                    ans2.append(ans[i])
            ans = ans2
            print(len(ans))
            print(*ans)
            done = True
            break

        if not done:
            print(-1)











        # dd = defaultdict(list)
        # for i in range(n):
        #     for pf in getFactorization(arr[i]):
        #         dd[pf].append(i)
        
        # # print(dict(dd))

        # vis = [False] * n
        # q = deque([u])
        # vis[u] = True
        # parent = [-1] * n
        # while q:
        #     idx = q.popleft()
        #     for pf in getFactorization(arr[idx]):
        #         for child in dd[pf]:
        #             if not vis[child]:
        #                 vis[child] = True
        #                 parent[child] = idx
        #                 q.append(child)

        # if not vis[v]:
        #     print(-1)
        #     continue

        # ans = []
        # while v != -1:
        #     ans.append(v + 1)
        #     v = parent[v]
        
        # print(len(ans))
        # print(*ans[::-1])











        # for x in q:
        #     parent[x] = -2
        # last = -1
        # while q:
        #     node = q.popleft()
        #     for i in g[node]:
        #         if parent[i] == -1:
        #             parent[i] = node
        #             q.append(i)
        #             if i in dest:
        #                 last = i
        #                 break
        
        # if last == -1:
        #     print(-1)
        #     continue
        
        # print(parent)
        # print(last)
        # path = [v + 1]
        
        # while last >= 0:
        #     last = parent[last]
        #     path.append(dd[last][0] + 1)
        
        # print(len(path))
        # print(*path[::-1])


        # dd = defaultdict(list)
        # for i in range(n):
        #     for pf in getFactorization(arr[i]):
        #         dd[pf].append(i)
        
        # print(dd)


        # g = [set() for i in range(n)]
        # for i in dd:
        #     for j in range(len(dd[i])-1):
        #         g[dd[i][j]].add(dd[i][j+1])
        #         g[dd[i][j+1]].add(dd[i][j])

        # for i in range(n):
        #     g[i] = list(g[i])

        # path = []
        # parent = [-1] * n
        # q = deque([u])
        # vis = [0]*n

        # while q:
        #     node = q.popleft()
        #     vis[node] = 1
        #     if node == v:
        #         break
        #     for i in g[node]:
        #         if not vis[i]:
        #             parent[i] = node
        #             q.append(i)
        
        # if parent[v] == -1:
        #     print(-1)
        #     return
        
        # while v != -1:
        #     path.append(v)
        #     v = parent[v]
        
        # print(len(path))
        # print(*[i+1 for i in path[::-1]])

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
