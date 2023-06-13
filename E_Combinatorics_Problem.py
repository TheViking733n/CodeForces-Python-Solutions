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
from itertools import accumulate


# INF = float("inf")
INF = 9223372036854775807
PI = 3.141592653589793
R = randrange(2, 1 << 32)
# R = 0          # Enable this for debugging of dict keys in myDict

# ========================= Main ==========================

M=998244353
# def make_nCr_mod(max_n=int(6e6+5), mod=M):
#     max_n = min(max_n, mod - 1)

#     fact, inv_fact = [0] * (max_n + 1), [0] * (max_n + 1)
#     fact[0] = 1
#     for i in range(max_n):
#         fact[i + 1] = fact[i] * (i + 1) % mod

#     inv_fact[-1] = pow(fact[-1], mod - 2, mod)
#     for i in reversed(range(max_n)):
#         inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod

#     def nCr_mod(n, r):
#         if n < r:
#             return 0
#         res = 1
#         while n or r:
#             a, b = n % mod, r % mod
#             if a < b:
#                 return 0
#             res = res * fact[a] % mod * inv_fact[b] % mod * inv_fact[a - b] % mod
#             n //= mod
#             r //= mod
#         return res

#     return nCr_mod


# # nCr = make_nCr_mod()

# MOD = 998244353
# MODF = float(MOD)
# ROOT = 3.0

# MAGIC = 6755399441055744.0
# SHRT = 65536.0

# MODF_INV = 1.0 / MODF
# SHRT_INV = 1.0 / SHRT

# fround = lambda x: (x + MAGIC) - MAGIC
# fmod = lambda a: a - MODF * fround(MODF_INV * a)
# fmul = lambda a, b, c=0.0: fmod(fmod(a * SHRT) * fround(SHRT_INV * b) + a * (b - SHRT * fround(b * SHRT_INV)) + c)


# def fpow(x, y):
#     if y == 0:
#         return 1.0

#     res = 1.0
#     while y > 1:
#         if y & 1 == 1:
#             res = fmul(res, x)
#         x = fmul(x, x)
#         y >>= 1

#     return fmul(res, x)


# def ntt(a, inv=False):
#     n = len(a)
#     w = [1.0] * (n >> 1)

#     w[1] = fpow(ROOT, (MOD - 1) // n)
#     if inv:
#         w[1] = fpow(w[1], MOD - 2)

#     for i in range(2, (n >> 1)):
#         w[i] = fmul(w[i - 1], w[1])

#     rev = [0] * n
#     for i in range(n):
#         rev[i] = rev[i >> 1] >> 1
#         if i & 1 == 1:
#             rev[i] |= n >> 1
#         if i < rev[i]:
#             a[i], a[rev[i]] = a[rev[i]], a[i]

#     step = 2
#     while step <= n:
#         half, diff = step >> 1, n // step
#         for i in range(0, n, step):
#             pw = 0
#             for j in range(i, i + half):
#                 v = fmul(w[pw], a[j + half])
#                 a[j + half] = a[j] - v
#                 a[j] += v
#                 pw += diff

#         step <<= 1

#     if inv:
#         inv_n = fpow(n, MOD - 2)
#         for i in range(n):
#             a[i] = round(fmul(a[i], inv_n))


# def ntt_conv(a, b):
#     s = len(a) + len(b) - 1
#     n = 1 << s.bit_length()

#     a.extend([0.0] * (n - len(a)))
#     b.extend([0.0] * (n - len(b)))

#     ntt(a)
#     ntt(b)

#     for i in range(n):
#         a[i] = fmul(a[i], b[i])

#     ntt(a, True)
#     del a[s:]


inf = 2 ** 63 - 1
mod = 998244353
"""
Reference
https://github.com/atcoder/ac-library/blob/master/atcoder/convolution.hpp
https://github.com/atcoder/ac-library/blob/master/atcoder/internal_math.hpp
https://github.com/atcoder/ac-library/blob/master/document_en/convolution.md
https://github.com/atcoder/ac-library/blob/master/document_ja/convolution.md
"""
mod = 998244353
def primitive_root(m):
    if m == 2:
        return 1
    if m == 167772161:
        return 3
    if m == 469762049:
        return 3
    if m == 754974721:
        return 11
    if m == 998244353:
        return 3
    divs = [0] * 20
    divs[0] = 2
    cnt = 1
    x = (m - 1) // 2
    while x % 2 == 0:
        x //= 2
    i = 3
    while i * i <= x:
        if x % i == 0:
            divs[cnt] = i
            cnt += 1
            while x % i == 0:
                x //= i
        i += 2
    if x > 1:
        divs[cnt] = x
        cnt += 1
    g = 2
    while True:
        ok = True
        for i in range(cnt):
            if pow(g, (m - 1) // divs[i], m) == 1:
                ok = False
                break
        if ok:
            return g
        g += 1
 
 
class FFT_INFO:
    def __init__(self):
        self.g = primitive_root(mod)
        self.rank2 = ((mod - 1) & (1 - mod)).bit_length() - 1
        self.root = [0] * (self.rank2 + 1)
        self.root[self.rank2] = pow(self.g, (mod - 1) >> self.rank2, mod)
        self.iroot = [0] * (self.rank2 + 1)
        self.iroot[self.rank2] = pow(self.root[self.rank2], mod - 2, mod)
        for i in range(self.rank2 - 1, -1, -1):
            self.root[i] = self.root[i + 1] * self.root[i + 1] % mod
            self.iroot[i] = self.iroot[i + 1] * self.iroot[i + 1] % mod
 
        self.rate2 = [0] * max(0, self.rank2 - 1)
        self.irate2 = [0] * max(0, self.rank2 - 1)
        prod = 1
        iprod = 1
        for i in range(self.rank2 - 1):
            self.rate2[i] = self.root[i + 2] * prod % mod
            self.irate2[i] = self.iroot[i + 2] * iprod % mod
            prod *= self.iroot[i + 2]
            prod %= mod
            iprod *= self.root[i + 2]
            iprod %= mod
 
        self.rate3 = [0] * max(0, self.rank2 - 2)
        self.irate3 = [0] * max(0, self.rank2 - 2)
        prod = 1
        iprod = 1
        for i in range(self.rank2 - 2):
            self.rate3[i] = self.root[i + 3] * prod % mod
            self.irate3[i] = self.iroot[i + 3] * iprod % mod
            prod *= self.iroot[i + 3]
            prod %= mod
            iprod *= self.root[i + 3]
            iprod %= mod
 
 
info = FFT_INFO()
 
 
def butterfly(a):
    n = len(a)
    h = (n - 1).bit_length()
 
    length = 0
    while length < h:
        if h - length == 1:
            p = 1 << (h - length - 1)
            rot = 1
            for s in range(1 << length):
                offset = s << (h - length)
                for i in range(p):
                    l = a[i + offset]
                    r = a[i + offset + p] * rot % mod
                    a[i + offset] = (l + r) % mod
                    a[i + offset + p] = (l - r) % mod
                if s + 1 != (1 << length):
                    rot *= info.rate2[(~s & -~s).bit_length() - 1]
                    rot %= mod
            length += 1
        else:
            # 4-base
            p = 1 << (h - length - 2)
            rot = 1
            imag = info.root[2]
            for s in range(1 << length):
                rot2 = rot * rot % mod
                rot3 = rot2 * rot % mod
                offset = s << (h - length)
                for i in range(p):
                    a0 = a[i + offset]
                    a1 = a[i + offset + p] * rot
                    a2 = a[i + offset + 2 * p] * rot2
                    a3 = a[i + offset + 3 * p] * rot3
                    a1na3imag = (a1 - a3) % mod * imag
                    a[i + offset] = (a0 + a2 + a1 + a3) % mod
                    a[i + offset + p] = (a0 + a2 - a1 - a3) % mod
                    a[i + offset + 2 * p] = (a0 - a2 + a1na3imag) % mod
                    a[i + offset + 3 * p] = (a0 - a2 - a1na3imag) % mod
                if s + 1 != (1 << length):
                    rot *= info.rate3[(~s & -~s).bit_length() - 1]
                    rot %= mod
            length += 2
 
 
def butterfly_inv(a):
    n = len(a)
    h = (n - 1).bit_length()
 
    length = h  # a[i, i+(n<<length), i+2*(n>>length), ...] is transformed 
    while length:
        if length == 1:
            p = 1 << (h - length)
            irot = 1
            for s in range(1 << (length - 1)):
                offset = s << (h - length + 1)
                for i in range(p):
                    l = a[i + offset]
                    r = a[i + offset + p]
                    a[i + offset] = (l + r) % mod
                    a[i + offset + p] = (l - r) * irot % mod
                if s + 1 != (1 << (length - 1)):
                    irot *= info.irate2[(~s & -~s).bit_length() - 1]
                    irot %= mod
            length -= 1
        else:
            # 4-base
            p = 1 << (h - length)
            irot = 1
            iimag = info.iroot[2]
            for s in range(1 << (length - 2)):
                irot2 = irot * irot % mod
                irot3 = irot2 * irot % mod
                offset = s << (h - length + 2)
                for i in range(p):
                    a0 = a[i + offset]
                    a1 = a[i + offset + p]
                    a2 = a[i + offset + 2 * p]
                    a3 = a[i + offset + 3 * p]
                    a2na3iimag = (a2 - a3) * iimag % mod
                    a[i + offset] = (a0 + a1 + a2 + a3) % mod
                    a[i + offset + p] = (a0  - a1 + a2na3iimag) * irot % mod
                    a[i + offset + 2 * p] = (a0 + a1 - a2 - a3) * irot2 % mod
                    a[i + offset + 3 * p] = (a0  - a1 - a2na3iimag) * irot3 % mod
                if s + 1 != (1 << (length - 2)):
                    irot *= info.irate3[(~s & -~s).bit_length() - 1]
                    irot %= mod
            length -= 2
 
 
def convolution_naive(a, b):
    n = len(a)
    m = len(b)
    ans = [0] * (n + m - 1)
    if n < m:
        for j in range(m):
            for i in range(n):
                ans[i + j] += a[i] * b[j]
                ans[i + j] %= mod
    else:
        for i in range(n):
            for j in range(m):
                ans[i + j] += a[i] * b[j]
                ans[i + j] %= mod
    return ans
 
 
def convolution_fft(a, b):
    a = a.copy()
    b = b.copy()
    n = len(a)
    m = len(b)
    z = 1 << (n + m - 2).bit_length()
    a += [0] * (z - n)
    butterfly(a)
    b += [0] * (z - m)
    butterfly(b)
    for i in range(z):
        a[i] *= b[i]
        a[i] %= mod
    butterfly_inv(a)
    a = a[:n + m - 1]
    iz = pow(z, mod - 2, mod)
    for i in range(n + m - 1):
        a[i] *= iz
        a[i] %= mod
    return a
 
 
def convolution(a, b):
    n = len(a)
    m = len(b)
    if not n or not m:
        return []
    if min(n, m) <= 60:
        return convolution_naive(a, b)
    return convolution_fft(a, b)



def mod_inv(x):
    return powm(x, M-2, M)

def main():
    TestCases = 1
    
    for _ in range(TestCases):
        n, a1, x, y, m, k = [int(i) for i in input().split()]
        a = [a1]
        for _ in range(n-1):
            a.append((a[-1]*x + y) % m)
        
        for _ in range(k+1):
            a = accumulate(a, lambda x, y: (x+y)%M)

        

        # # pol = [nCr(i, k) for i in range(1, n + 1)]
        # pol = []

        # # fact = [1]
        # f = 1
        # # print(mod_inv(0))
        # factInv = [1]
        # kInv = 1
        # for i in range(1, k + 1):
        #     kInv = (kInv * mod_inv(i)) % M
        # for i in range(n):
        #     # fact.append((fact[-1]*(i+1)) % M)
        #     f = (f * (i+1)) % M
        #     factInv.append((factInv[-1] * mod_inv(i+1)) % M)
        #     if i+1 - k < 0:
        #         pol.append(0)
        #         continue
        #     # pol.append((fact[i+1] * kInv * factInv[i+1-k]) % M)
        #     pol.append((f * kInv * factInv[i+1-k]) % M)
        

        # a = convolution(a, pol)
        # # print(a)
        # # print(n, len(a))
        a = list(a)
        ans = 0
        for i in range(n-k+1):
            ans ^= a[i] * (i + k)
        
        print(ans)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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