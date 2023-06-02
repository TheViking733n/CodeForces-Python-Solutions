# CHECK THIS
def EulerTour(g, root=0):
    res = []
    n = len(g)
    par = [-1]*n
    stack = [(root, True)]
    while stack:
        u, go = stack.pop()
        res.append(u)
        if go:
            for v in g[u]:
                if v == par[u]: continue
                par[v] = u
                stack.append((u, False))
                stack.append((v, True))
    return res

def EulerTour(n, X, i0 = 0):
    Q = [~i0, i0]
    ct = -1
    ET = []
    ET1 = [0] * n
    ET2 = [0] * n
    de = -1
    while Q:
        i = Q.pop()
        if i < 0:
            ET2[~i] = ct
            de -= 1
            continue
        if i >= 0:
            ET.append(i)
            ct += 1
            if ET1[i] == 0: ET1[i] = ct
            de += 1
            DE[i] = de
        for a in X[i][::-1]:
            if a != P[i]:
                P[a] = i
                for k in range(len(X[a])):
                    if X[a][k] == i:
                        del X[a][k]
                        break
                Q.append(~a)
                Q.append(a)
    return (ET, ET1, ET2)


####################################

import sys,os,io
# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
input = sys.stdin.buffer.readline

import math

sys.modules["hashlib"] = sys.sha512 = sys
import random

RANDOM = random.getrandbits(32)

class Wrapper(int):
    def __init__(self, x):
        int.__init__(x)
    def __hash__(self):
        return super(Wrapper, self).__hash__() ^ RANDOM

from collections import defaultdict
class DefaultDict:
    def __init__(self, default=None):
        self.default = default
        self.x = random.randrange(1, 1 << 31)
        self.dd = defaultdict(default)
 
    def __repr__(self):
        return "{"+", ".join(f"{k ^ self.x}: {v}" for k, v in self.dd.items())+"}"
 
    def __eq__(self, other):
        return set(self.dd.items()) == set(other.dd.items())
 
    def __or__(self, other):
        res = DefaultDict(self.default)
        for k, v in self.dd: res[k] = v
        for k, v in other.dd: res[k] = v
        return res
 
    def __len__(self):
        return len(self.dd)
 
    def __getitem__(self, item):
        return self.dd[item ^ self.x]
 
    def __setitem__(self, key, value):
        self.dd[key ^ self.x] = value
 
    def __delitem__(self, key):
        del self.dd[key ^ self.x]
 
    def __contains__(self, item):
        return item ^ self.x in self.dd
 
    def items(self):
        for k, v in self.dd.items(): yield (k ^ self.x, v)
 
    def keys(self):
        for k in self.dd: yield k ^ self.x
 
    def values(self):
        for v in self.dd.values(): yield v
 
    def __iter__(self):
        for k in self.dd: yield k ^ self.x
 
class Counter(DefaultDict):
    def __init__(self, aa=[]):
        super().__init__(int)
        for a in aa: self.dd[a ^ self.x] += 1
 
    def __add__(self, other):
        res = Counter()
        for k, v in self.items(): res[k] = v
        for k, v in other.items(): res[k] += v
        return res
 
    def __sub__(self, other):
        res = Counter()
        for k, v in self.items(): res[k] = v
        for k, v in other.items(): res[k] -= v
        return res
 
    def __and__(self, other):
        res = Counter()
        for k in self:
            v = min(self[k], other[k])
            if v > 0: res[k] = v
        return res
 
    def __eq__(self, other):
        if len(self) != len(other): return False
        for k, v in self.items():
            if other[k] != v: return False
        return True
 
    def __or__(self, other):
        res = Counter()
        for k in set(self) | set(other):
            v = max(self[k], other[k])
            if v > 0: res[k] = v
        return res
 
    def __iter__(self):
        for k in self.dd: yield k ^ self.x
 
class Set:
    def __init__(self, aa=[]):
        self.x = random.randrange(1, 1 << 31)
        self.st = set()
        for a in aa: self.st.add(a ^ self.x)
 
    def __repr__(self):
        return "{"+", ".join(str(k ^ self.x) for k in self.st)+"}"
 
    def __len__(self):
        return len(self.st)
 
    def add(self, item):
        self.st.add(item ^ self.x)
 
    def discard(self, item):
        self.st.discard(item ^ self.x)
 
    def __contains__(self, item):
        return item ^ self.x in self.st
 
    def __iter__(self):
        for k in self.st: yield k ^ self.x
 
    def pop(self):
        return self.st.pop() ^ self.x
 
    def __or__(self, other):
        res = Set(self)
        for a in other: res.add(a)
        return res
 
    def __and__(self, other):
        res = Set()
        for a in self:
            if a in other: res.add(a)
        for a in other:
            if a in self: res.add(a)
        return res


def invMod(a,m):
    return pow(a,m-2,m)

import re
def cntPat(s,pat):
    return len(re.findall("(?=%s)" % pat, s))


# =================== PRIME FACTORS (LOG N) =====================
 
# factors = [i for i in range(int(1e6)+5)]
# for i in range(2, 1005):
#     if factors[i] != i:
#         continue
#     for j in range(i, len(factors), i):
#         factors[j] = i
 
# def do(num):
#     while(num > 1):
#         x = factors[num]
#         try:
#             primes[x] += 1
#         except:
#             primes[x] = 1
#         while(num % x == 0):
#             num = num // x


# ==================== PRIME FACTORS (SQRT N) =====================
def primeFactor(N):
    i, n, ret, d, sq = 2, N, {}, 2, 99
    while i <= sq:
        k = 0
        while n % i == 0: n, k, ret[i] = n//i, k+1, k+1
        if k > 0 or i == 97: sq = int(n**(1/2)+0.5)
        if i < 4: i = i * 2 - 1
        else: i, d = i+d, d^6
    if n > 1: ret[n] = 1
    return ret

def divisors(N):
    pf = primeFactor(N)
    ret = [1]
    for p in pf:
        ret_prev = ret
        ret = []
        for i in range(pf[p]+1):
            for r in ret_prev:
                ret.append(r * (p ** i))
    return sorted(ret)
    
def primeFactors(n):
    ans = []
    while not n%2:
        ans.append(2)
        n//=2
    for i in range(3,int(math.sqrt(n))+1,2):
        while not n%i:
            ans.append(i)
            n//=i
    if n > 2:
        ans.append(n)
    return ans

# =================== LINEAR SIEVE ===================
def Prime(n):
    c=0
    prime=[]
    flag=[0]*(n+1)
    for i in range(2,n+1):
        if not flag[i]:
            prime.append(i)
            c+=1
        for j in range(c):
            if i*prime[j]>n: break
            flag[i*prime[j]]=prime[j]
            if i%prime[j]==0: break
    return prime

# =================== LINEAR SEIEVE + FINDING ALL DIVISORS ===================
# maxn = 20000001
# primes = []
# spf = [0]*(maxn+1)
# for i in range(2, maxn):
#     if spf[i]==0:
#         spf[i]=i
#         primes.append(i)
#     j = 0
#     while j < len(primes) and primes[j] <= spf[i] and primes[j]*i <= maxn:
#         spf[primes[j]*i] = primes[j]
#         j += 1

# cntPrime = [0]*(maxn+1)
# for i in range(2,maxn+1):
#     lpf = i//spf[i]
#     cntPrime[i] += cntPrime[lpf] + (spf[lpf] != spf[i])

# def divisors(n):
#     pf = []
#     while n > 1:
#         if len(pf) == 0 or pf[-1][0] != spf[n]:
#             pf.append([spf[n],1])
#         else:
#             pf[-1][1] += 1
 
#         n //= spf[n]
 
#     divs = [1]
#     for prime, count in pf:
#         l = len(divs)
#         prime_pow = 1
 
#         for i in range(count):
#             prime_pow *= prime
#             for j in range(l):
#                 divs.append(divs[j]*prime_pow)
#     return divs


# =================== MILLER RABIN =====================
def isPrimeMR(n):
    d = n - 1
    d = d // (d & -d)
    L = [2, 7, 61] if n < 1<<32 else [2, 3, 5, 7, 11, 13, 17] if n < 1<<48 else [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    # L = [2, 3, 5, 7, 11, 13, 17]
    # if n in L:
    #     return 1
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
    return ret

def divisors(n):
    res = [1]
    prime = primeFactor(n)
    for p in prime:
        newres = []
        for d in res:
            for j in range(prime[p]+1):
                newres.append(d*p**j)
        res = newres
    res.sort()
    return res


def nxt_larger(a):
    n = len(a)
    ans = [-1]*n
    stack = []
    for i in range (n):
        while(len(stack)>0 and stack[-1][0]<a[i]):
            curr = stack.pop()
            ans[curr[1]] = i
        stack.append([a[i],i])
    return ans

def prev_larger(a):
    n = len(a)
    a.reverse()
    ans = [-1]*n
    stack = []
    for i in range (n):
        while(len(stack)>0 and stack[-1][0]<a[i]):
            curr = stack.pop()
            ans[curr[1]] = n-i-1
        stack.append([a[i],i])
    ans.reverse()
    a.reverse()
    return ans


# ============= FAST IO ==============
import os
import sys
from io import BytesIO, IOBase

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
 
 
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")


# ========= SEGMENT TREE ==========
class SegmentTree():
    def __init__(self, init, unitX, f):
        self.f = f # (X, X) -> X
        self.unitX = unitX
        self.f = f
        if type(init) == int:
            self.n = init
            self.n = 1 << (self.n - 1).bit_length()
            self.X = [unitX] * (self.n * 2)
        else:
            self.n = len(init)
            self.n = 1 << (self.n - 1).bit_length()
            self.X = [unitX] * self.n + init + [unitX] * (self.n - len(init))
            for i in range(self.n-1, 0, -1):
                self.X[i] = self.f(self.X[i*2], self.X[i*2|1])
        
    def update(self, i, x):
        i += self.n
        self.X[i] = x
        i >>= 1
        while i:
            self.X[i] = self.f(self.X[i*2], self.X[i*2|1])
            i >>= 1
    
    def getvalue(self, i):
        return self.X[i + self.n]
    
    def getrange(self, l, r):
        l += self.n
        r += self.n
        al = self.unitX
        ar = self.unitX
        while l < r:
            if l & 1:
                al = self.f(al, self.X[l])
                l += 1
            if r & 1:
                r -= 1
                ar = self.f(self.X[r], ar)
            l >>= 1
            r >>= 1
        return self.f(al, ar)
    
    # Find r s.t. calc(l, ..., r-1) = True and calc(l, ..., r) = False
    def max_right(self, l, z):
        if l >= self.n: return self.n
        l += self.n
        s = self.unitX
        while 1:
            while l % 2 == 0:
                l >>= 1
            if not z(self.f(s, self.X[l])):
                while l < self.n:
                    l *= 2
                    if z(self.f(s, self.X[l])):
                        s = self.f(s, self.X[l])
                        l += 1
                return l - self.n
            s = self.f(s, self.X[l])
            l += 1
            if l & -l == l: break
        return self.n
    
    # Find l s.t. calc(l, ..., r-1) = True and calc(l-1, ..., r-1) = False
    def min_left(self, r, z):
        if r <= 0: return 0
        r += self.n
        s = self.unitX
        while 1:
            r -= 1
            while r > 1 and r % 2:
                r >>= 1
            if not z(self.f(self.X[r], s)):
                while r < self.n:
                    r = r * 2 + 1
                    if z(self.f(self.X[r], s)):
                        s = self.f(self.X[r], s)
                        r -= 1
                return r + 1 - self.n
            s = self.f(self.X[r], s)
            if r & -r == r: break
        return 0
    
    def debug(self):
        print("debug")
        print([self.getvalue(i) for i in range(min(self.n, 20))])



# ========= DELETABLE MIN HEAP ==========

from heapq import heappush, heappop
class DeletableMinPQ():
    def __init__(self):
        self.H = []
        self.HC = defaultdict(int)
        self.size = 0
    def push(self, x):
        heappush(self.H, x)
        self.HC[x] += 1
        self.size += 1
    def pop(self):
        assert len(self.H) > 0
        t = heappop(self.H)
        while not self.HC[t]:
            t = heappop(self.H)
        self.HC[t] -= 1
        self.size -= 1
        return t
    def min(self):
        assert len(self.H) > 0
        t = self.H[0]
        while not self.HC[t]:
            heappop(self.H)
            t = self.H[0]
        return t
    def remove(self, x):
        if self.HC[x] > 0:
            self.HC[x] -= 1
            self.size -= 1
            return True
        return False
    def __len__(self):
        return self.size
    def __bool__(self):
        return len(self.H) > 0
    def __repr__(self):
        items = []
        for k in self.HC:
            items.extend([k]*self.HC[k])
        return str(sorted(items))



# ========= FIBONACCI HEAP ==========
class FibonacciHeap():
    def __init__(self, mm):
        self.inf = 1 << 62 ############
        self.mm = mm
        self.roots = [[] for _ in range(mm)]
        self.min = self.inf
        self.minroot = None
    
    def add(self, v):
        nd = self.node(v)
        self.add_node(nd)
        return nd
    
    def add_node(self, nd):
        k = nd.order
        if nd.value < self.min:
            self.min = nd.value
            self.minroot = nd
        self.roots[k].append(nd)
    
    def setmin(self):
        mi = self.inf
        mirt = None
        for i, rt in enumerate(self.roots):
            while len(rt) >= 2:
                nd1 = rt.pop()
                nd2 = rt.pop()
                self.roots[i+1].append(nd1.meld(nd2))
            if len(rt) and rt[0].value < mi:
                mi = rt[0].value
                mirt = rt[0]
        self.min = mi
        self.minroot = mirt
        return self.minroot
    
    def pop(self):
        nd = self.minroot
        mi = nd.value
        self.roots[nd.order].remove(nd)
        ch = nd.repChild
        if ch:
            nd = ch.right
            while 1:
                nnd = nd.right
                self.add_node(nd)
                l = nd.left
                r = nd.right
                if r != nd:
                    nd.right = nd
                    nd.left = nd
                    l.right = r
                    r.left = l
                nd.parent = None
                if nd == ch:
                    break
                nd = nnd
        self.setmin()
        return mi
    
    class node():
        def __init__(self, value):
            self.parent = None
            self.left = self
            self.right = self
            self.repChild = None
            self.order = 0
            self.marked = 0
            self.value = value
        
        def meld(self, other):
            if self.value > other.value:
                return other.meld(self)
            other.parent = self
            if not self.repChild:
                self.repChild = other
            else:
                l = self.repChild
                r = l.right
                l.right = other
                r.left = other
                other.left = l
                other.right = r
            self.order += 1
            return self
    
    def movetop(self, nd):
        p = nd.parent
        nd.marked = 0
        if not p: return nd
        l = nd.left
        r = nd.right
        if r != nd:
            p.repChild = r
            nd.right = nd
            nd.left = nd
            l.right = r
            r.left = l
        else:
            p.repChild = None
        nd.parent = None
        self.add_node(nd)
        if not p.parent:
            self.roots[p.order].remove(p)
            p.order -= 1
            self.add_node(p)
        
    def prioritize(self, nd, v):
        p = nd.parent
        nd.value = v
        if v < self.min:
            self.min = v
            self.minroot = nd
        if not p or p.value <= v:
            return nd
        self.movetop(nd)
        nn = p
        while nn.parent:
            if nn.marked == 0:
                nn.marked = 1
                break
            else:
                p = nn.parent
                self.movetop(nn)
                nn = p
        return nd


# ========= Jump On Tree, LCA, Binary lifting ==========

class JumpOnTree:
    def __init__(self, edges, root=0):
        self.n = len(edges)
        self.edges = edges
        self.root = root
        self.logn = (self.n - 1).bit_length()
        self.depth = [-1] * self.n
        self.depth[self.root] = 0
        self.parent = [[-1] * self.n for _ in range(self.logn)]
        self.dfs()
        self.doubling()
    
    def dfs(self):
        stack = [self.root]
        while stack:
            u = stack.pop()
            for v in self.edges[u]:
                if self.depth[v] == -1:
                    self.depth[v] = self.depth[u] + 1
                    self.parent[0][v] = u
                    stack.append(v)
 
    def doubling(self):
        for i in range(1, self.logn):
            for u in range(self.n):
                p = self.parent[i - 1][u]
                if p != -1:
                    self.parent[i][u] = self.parent[i - 1][p]
    
    def lca(self, u, v):
        du = self.depth[u]
        dv = self.depth[v]
        if du > dv:
            du, dv = dv, du
            u, v = v, u
        
        d = dv - du
        i = 0
        while d > 0:
            if d & 1:
                v = self.parent[i][v]
            d >>= 1
            i += 1
        if u == v:
            return u
        
        logn = (du - 1).bit_length()
        for i in range(logn - 1, -1, -1):
            pu = self.parent[i][u]
            pv = self.parent[i][v]
            if pu != pv:
                u = pu
                v = pv
        return self.parent[0][u]
 
    def jump(self, u, v, k):
        if k == 0:
            return u
        p = self.lca(u, v)
        d1 = self.depth[u] - self.depth[p]
        d2 = self.depth[v] - self.depth[p]
        if d1 + d2 < k:
            return -1
        if k <= d1:
            d = k
        else:
            u = v
            d = d1 + d2 - k
        i = 0
        while d > 0:
            if d & 1:
                u = self.parent[i][u]
            d >>= 1
            i += 1
        return u


# ========= Lazy Segment Tree (update) ==========

def segfunc(x,y):
    return max(x,y)
class LazySegTree_RUQ:
    def __init__(self,init_val,segfunc,ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1<<(n-1).bit_length()
        self.tree = [ide_ele]*2*self.num
        self.lazy = [None]*2*self.num
        for i in range(n):
            self.tree[self.num+i] = init_val[i]
        for i in range(self.num-1,0,-1):
            self.tree[i] = self.segfunc(self.tree[2*i],self.tree[2*i+1])
    def gindex(self,l,r):
        l += self.num
        r += self.num
        lm = l>>(l&-l).bit_length()
        rm = r>>(r&-r).bit_length()
        while r>l:
            if l<=lm:
                yield l
            if r<=rm:
                yield r
            r >>= 1
            l >>= 1
        while l:
            yield l
            l >>= 1
    def propagates(self,*ids):
        for i in reversed(ids):
            v = self.lazy[i]
            if v is None:
                continue
            self.lazy[i] = None
            self.lazy[2*i] = v
            self.lazy[2*i+1] = v
            self.tree[2*i] = v
            self.tree[2*i+1] = v
    def update(self,l,r,x):
        ids = self.gindex(l,r)
        self.propagates(*self.gindex(l,r))
        l += self.num
        r += self.num
        while l<r:
            if l&1:
                self.lazy[l] = x
                self.tree[l] = x
                l += 1
            if r&1:
                self.lazy[r-1] = x
                self.tree[r-1] = x
            r >>= 1
            l >>= 1
        for i in ids:
            self.tree[i] = self.segfunc(self.tree[2*i], self.tree[2*i+1])
    def query(self,l,r):
        ids = self.gindex(l,r)
        self.propagates(*self.gindex(l,r))
        res = self.ide_ele
        l += self.num
        r += self.num
        while l<r:
            if l&1:
                res = self.segfunc(res,self.tree[l])
                l += 1
            if r&1:
                res = self.segfunc(res,self.tree[r-1])
            l >>= 1
            r >>= 1
        return res
