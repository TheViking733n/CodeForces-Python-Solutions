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

# import cmath

# MOD = 10**9 + 7

# n, M = [int(i) for i in input().split()]



# def fft(a, inv=False):
#     n = len(a)
#     w = [cmath.rect(1, (-2 if inv else 2) * cmath.pi * i / n) for i in range(n >> 1)]
#     rev = [0] * n
#     for i in range(n):
#         rev[i] = rev[i >> 1] >> 1
#         if i & 1:
#             rev[i] |= n >> 1
#         if i < rev[i]:
#             a[i], a[rev[i]] = a[rev[i]], a[i]

#     step = 2
#     while step <= n:
#         half, diff = step >> 1, n // step
#         for i in range(0, n, step):
#             pw = 0
#             for j in range(i, i + half):
#                 v = a[j + half] * w[pw]
#                 a[j + half] = a[j] - v
#                 a[j] += v
#                 pw += diff
#         step <<= 1

#     if inv:
#         for i in range(n):
#             a[i] /= n


# def fft_conv(a, b):
#     s = len(a) + len(b) - 1
#     n = 1 << s.bit_length()
#     a.extend([0.0] * (n - len(a)))
#     b.extend([0.0] * (n - len(b)))

#     fft(a), fft(b)
#     for i in range(n):
#         a[i] *= b[i]
#     fft(a, True)

#     a = [round(a[i].real) % M for i in range(s)]
#     return a


#======================================================

# def popcount(x: int) -> int:
#     x = ((x >> 1)  & 0x55555555) + (x & 0x55555555)
#     x = ((x >> 2)  & 0x33333333) + (x & 0x33333333)
#     x = ((x >> 4)  & 0x0f0f0f0f) + (x & 0x0f0f0f0f)
#     x = ((x >> 8)  & 0x00ff00ff) + (x & 0x00ff00ff)
#     x = ((x >> 16) & 0x0000ffff) + (x & 0x0000ffff)
#     return x

# def bit_reverse(x: int) -> int:
#     x = (x >> 16) | (x << 16)
#     x = ((x >> 8) & 0x00FF00FF) | ((x << 8) & 0xFF00FF00)
#     x = ((x >> 4) & 0x0F0F0F0F) | ((x << 4) & 0xF0F0F0F0)
#     x = ((x >> 2) & 0x33333333) | ((x << 2) & 0xCCCCCCCC)
#     x = ((x >> 1) & 0x55555555) | ((x << 1) & 0xAAAAAAAA)
#     return x

# def tzcount(x: int) -> int:
#     return popcount(~x & (x - 1))

# def lzcount(x: int) -> int:
#     return tzcount(bit_reverse(x))

# def primitive_root(m: int) -> int:
#     if m == 2: return 1
#     if m == 998244353: return 3
#     divs = [0] * 20
#     divs[0] = 2
#     cnt = 1
#     x = (m - 1) // 2
#     while x % 2 == 0: x //= 2
#     i = 3
#     while i * i <= x:
#         if x % i == 0:
#             divs[cnt] = i
#             cnt += 1
#             while x % i == 0: x //= i
#         i += 2
#     if x > 1:
#         divs[cnt] = x
#         cnt += 1
#     g = 2
#     while True:
#         for i in range(cnt):
#             if pow(g, (m - 1) // divs[i], m) == 1: break
#         else:
#             return g
#         g += 1

# def inv_gcd(a: int, b: int) -> int:
#     a %= b
#     if a == 0: return b, 0
#     s = b
#     t = a
#     m0 = 0
#     m1 = 1
#     while t:
#         u = s // t
#         s -= t * u
#         m0 -= m1 * u
#         s, t = t, s
#         m0, m1 = m1, m0
#     if m0 < 0: m0 += b // s
#     return s, m0

# from typing import List, Tuple

# def crt(r: List[int], m: List[int]) -> Tuple[int, int]:
#     assert len(r) == len(m)
#     n = len(r)
#     r0 = 0
#     m0 = 1
#     for i in range(n):
#         assert 1 <= m[i]
#         r1 = r[i] % m[i]
#         m1 = m[i]
#         if m0 < m1:
#             r0, r1 = r1, r0
#             m0, m1 = m1, m0
#         if m0 % m1 == 0:
#             if r0 % m1 != r1: return 0, 0
#             continue
#         g, im = inv_gcd(m0, m1)
#         u1 = m1 // g
#         if (r1 - r0) % g: return 0, 0
#         x = (r1 - r0) // g * im % u1
#         r0 += x * m0
#         m0 *= u1
#         if (r0 < 0): r0 += m0
#     return r0, m0

# from typing import List, Callable, Union, Optional

# class Convolution():
#     def __init__(self, mod: Union[Callable[[None], int], int]) -> None:
#         self.mod = mod
#         if isinstance(mod, int): self.mod = lambda: mod
#         g = primitive_root(self.mod())
#         self.rank2 = rank2 = tzcount(self.mod() - 1)
#         self.root = root = [0] * (rank2 + 1)
#         self.iroot = iroot = [0] * (rank2 + 1)
#         self.rate2 = rate2 = [0] * max(0, rank2 - 1)
#         self.irate2 = irate2 = [0] * max(0, rank2 - 1)
#         self.rate3 = rate3 = [0] * max(0, rank2 - 2)
#         self.irate3 = irate3 = [0] * max(0, rank2 - 2)
#         root[rank2] = pow(g, (self.mod() - 1) >> rank2, self.mod())
#         iroot[rank2] = pow(root[rank2], self.mod() - 2, self.mod())
#         for i in range(rank2)[::-1]:
#             root[i] = root[i + 1] * root[i + 1] % self.mod()
#             iroot[i] = iroot[i + 1] * iroot[i + 1] % self.mod()
#         prod = 1
#         iprod = 1
#         for i in range(rank2 - 1):
#             rate2[i] = root[i + 2] * prod % self.mod()
#             irate2[i] = iroot[i + 2] * iprod % self.mod()
#             prod *= iroot[i + 2]
#             prod %= self.mod()
#             iprod *= root[i + 2]
#             iprod %= self.mod()
#         prod = 1
#         iprod = 1
#         for i in range(rank2 - 2):
#             rate3[i] = root[i + 3] * prod % self.mod()
#             irate3[i] = iroot[i + 3] * iprod % self.mod()
#             prod *= iroot[i + 3]
#             prod %= self.mod()
#             iprod *= root[i + 3]
#             iprod %= self.mod()
#         self.imag = root[2]
#         self.iimag = iroot[2]

#     def butterfly(self, a: List[int]) -> None:
#         n = len(a)
#         h = (n - 1).bit_length()
#         len_ = 0
#         while len_ < h:
#             if h - len_ == 1:
#                 p = 1 << (h - len_ - 1)
#                 rot = 1
#                 for s in range(1 << len_):
#                     offset = s << (h - len_)
#                     for i in range(p):
#                         l = a[i + offset]
#                         r = a[i + offset + p] * rot % self.mod()
#                         a[i + offset] = (l + r) % self.mod()
#                         a[i + offset + p] = (l - r) % self.mod()
#                     if s + 1 != 1 << len_:
#                         rot *= self.rate2[(~s & -~s).bit_length() - 1]
#                         rot %= self.mod()
#                 len_ += 1
#             else:
#                 p = 1 << (h - len_ - 2)
#                 rot = 1
#                 for s in range(1 << len_):
#                     rot2 = rot * rot % self.mod()
#                     rot3 = rot2 * rot % self.mod()
#                     offset = s << (h - len_)
#                     for i in range(p):
#                         a0 = a[i + offset]
#                         a1 = a[i + offset + p] * rot
#                         a2 = a[i + offset + p * 2] * rot2
#                         a3 = a[i + offset + p * 3] * rot3
#                         a1na3imag = (a1 - a3) % self.mod() * self.imag
#                         a[i + offset] = (a0 + a2 + a1 + a3) % self.mod()
#                         a[i + offset + p] = (a0 + a2 - a1 - a3) % self.mod()
#                         a[i + offset + p * 2] = (a0 - a2 + a1na3imag) % self.mod()
#                         a[i + offset + p * 3] = (a0 - a2 - a1na3imag) % self.mod()
#                     if s + 1 != 1 << len_:
#                         rot *= self.rate3[(~s & -~s).bit_length() - 1]
#                         rot %= self.mod()
#                 len_ += 2

#     def butterfly_inv(self, a: List[int]) -> None:
#         n = len(a)
#         h = (n - 1).bit_length()
#         len_ = h
#         while len_:
#             if len_ == 1:
#                 p = 1 << (h - len_)
#                 irot = 1
#                 for s in range(1 << (len_ - 1)):
#                     offset = s << (h - len_ + 1)
#                     for i in range(p):
#                         l = a[i + offset]
#                         r = a[i + offset + p]
#                         a[i + offset] = (l + r) % self.mod()
#                         a[i + offset + p] = (l - r) * irot % self.mod()
#                     if s + 1 != (1 << (len_ - 1)):
#                         irot *= self.irate2[(~s & -~s).bit_length() - 1]
#                         irot %= self.mod()
#                 len_ -= 1
#             else:
#                 p = 1 << (h - len_)
#                 irot = 1
#                 for s in range(1 << (len_ - 2)):
#                     irot2 = irot * irot % self.mod()
#                     irot3 = irot2 * irot % self.mod()
#                     offset = s << (h - len_ + 2)
#                     for i in range(p):
#                         a0 = a[i + offset]
#                         a1 = a[i + offset + p]
#                         a2 = a[i + offset + p * 2]
#                         a3 = a[i + offset + p * 3]
#                         a2na3iimag = (a2 - a3) * self.iimag % self.mod()
#                         a[i + offset] = (a0 + a1 + a2 + a3) % self.mod()
#                         a[i + offset + p] = (a0 - a1 + a2na3iimag) * irot % self.mod()
#                         a[i + offset + p * 2] = (a0 + a1 - a2 - a3) * irot2 % self.mod()
#                         a[i + offset + p * 3] = (a0 - a1 - a2na3iimag) * irot3 % self.mod()
#                     if s + 1 != (1 << (len_ - 2)):
#                         irot *= self.irate3[(~s & -~s).bit_length() - 1]
#                         irot %= self.mod()
#                 len_ -= 2

#     def convolution(self, a: List[int], b: List[int]) -> List[int]:
#         n = len(a)
#         m = len(b)
#         assert n + m - 1 <= 1 << self.rank2
#         if not n or not m: return []
#         if min(n, m) <= 0:
#             if n < m:
#                 n, m = m, n
#                 a, b = b, a
#             res = [0] * (n + m - 1)
#             for i in range(n):
#                 for j in range(m):
#                     res[i + j] += a[i] * b[j]
#                     res[i + j] %= self.mod()
#             return res
#         z = 1 << (n + m - 2).bit_length()
#         a += [0] * (z - n)
#         b += [0] * (z - m)
#         self.butterfly(a)
#         self.butterfly(b)
#         for i in range(z):
#             a[i] *= b[i]
#             a[i] %= self.mod()
#         self.butterfly_inv(a)
#         a = a[:n + m - 1]
#         iz = pow(z, self.mod() - 2, self.mod())
#         for i in range(n + m - 1):
#             a[i] *= iz
#             a[i] %= self.mod()
#         return a

# class ArbitraryModConvolution():
#     def __init__(self, mod: Union[Callable[[None], int], int], fmt_mods: Optional[List[Union[Callable[[None], int], int]]] = None) -> None:
#         self.mod = mod
#         if isinstance(mod, int): self.mod = lambda: mod
#         if fmt_mods is None:
#             MODs = [998244353, 943718401, 918552577, 924844033, 985661441]
#             # 998244353 = 119 * 2^23 + 1
#             # 943718401 = 225 * 2^22 + 1
#             # 918552577 = 219 * 2^22 + 1
#             # 924844033 = 441 * 2^21 + 1
#             # 985661441 = 235 * 2^22 + 1
#             self.mods = []
#             mul = 1
#             for MOD in MODs:
#                 mul *= MOD
#                 self.mods.append(MOD)
#                 if mul > 2**20 * self.mod() * self.mod():
#                     break
#             else:
#                 raise ValueError("mod is too large") 
#             self.convs = [Convolution(MOD) for MOD in self.mods]
#             self.minrank2 = min([conv.rank2 for conv in self.convs])
#         else:
#             self.mods = []
#             mul = 1
#             for MOD in fmt_mods:
#                 if isinstance(MOD, int): MOD = lambda: MOD
#                 mul *= MOD()
#                 self.mods.append(MOD())
#             if mul < 2**20 * self.mod() * self.mod():
#                 raise ValueError("fmt_mods is too small")
#             self.convs = [Convolution(MOD) for MOD in fmt_mods]
#             self.minrank2 = min([conv.rank2 for conv in self.convs])

#     def convolution(self, a: List[int], b: List[int]) -> List[int]:
#         n = len(a)
#         m = len(b)
#         assert n + m - 1 <= 1 << self.minrank2
#         if not n or not m: return []
#         if min(n, m) <= 0:
#             if n < m:
#                 n, m = m, n
#                 a, b = b, a
#             res = [0] * (n + m - 1)
#             for i in range(n):
#                 for j in range(m):
#                     res[i + j] += a[i] * b[j]
#                     res[i + j] %= self.mod()
#             return res
#         cs = [self.convs[i].convolution([v % self.mods[i] for v in a], [v % self.mods[i] for v in b]) for i in range(len(self.mods))]
#         res = [0] * (n + m - 1)
#         mods = [self.mods[i] for i in range(len(self.mods))]
#         for i, v in enumerate(zip(*cs)):
#             cr, cm = crt(v, mods)
#             res[i] = cr % self.mod()
#         return res       
    
# import sys
# input = sys.stdin.buffer.readline

# n, M = map(int, input().split())

# conv = ArbitraryModConvolution(lambda: M, fmt_mods=[lambda: 998244353, lambda: 943718401, lambda: 918552577, lambda: 924844033, lambda: 985661441])



# def binary_exp_fft_conv(pol, exp):
#     ans = [1]
#     while exp > 0:
#         if exp & 1:
#             ans = conv.convolution(ans, pol)
#             # ntt_conv(ans, pol[:])
#         exp >>= 1
#         pol = conv.convolution(pol, pol)
#         # ntt_conv(pol, pol[:])

#     return ans


#============================================================
import sys
readline=sys.stdin.readline

mod = 998244353
imag = 911660635
iimag = 86583718
rate2 = (911660635, 509520358, 369330050, 332049552, 983190778, 123842337, 238493703, 975955924, 603855026, 856644456, 131300601,
              842657263, 730768835, 942482514, 806263778, 151565301, 510815449, 503497456, 743006876, 741047443, 56250497, 867605899)
irate2 = (86583718, 372528824, 373294451, 645684063, 112220581, 692852209, 155456985, 797128860, 90816748, 860285882, 927414960,
               354738543, 109331171, 293255632, 535113200, 308540755, 121186627, 608385704, 438932459, 359477183, 824071951, 103369235)
rate3 = (372528824, 337190230, 454590761, 816400692, 578227951, 180142363, 83780245, 6597683, 70046822, 623238099,
              183021267, 402682409, 631680428, 344509872, 689220186, 365017329, 774342554, 729444058, 102986190, 128751033, 395565204)
irate3 = (509520358, 929031873, 170256584, 839780419, 282974284, 395914482, 444904435, 72135471, 638914820, 66769500,
               771127074, 985925487, 262319669, 262341272, 625870173, 768022760, 859816005, 914661783, 430819711, 272774365, 530924681)

def butterfly(a):
    n = len(a)
    h = (n - 1).bit_length()
    len_ = 0
    while len_ < h:
        if h - len_ == 1:
            p = 1 << (h - len_ - 1)
            rot = 1
            for s in range(1 << len_):
                offset = s << (h - len_)
                for i in range(p):
                    l = a[i + offset]
                    r = a[i + offset + p] * rot % mod
                    a[i + offset] = (l + r) % mod
                    a[i + offset + p] = (l - r) % mod
                if s + 1 != 1 << len_:
                    rot *= rate2[(~s & -~s).bit_length() - 1]
                    rot %= mod
            len_ += 1
        else:
            p = 1 << (h - len_ - 2)
            rot = 1
            for s in range(1 << len_):
                rot2 = rot * rot % mod
                rot3 = rot2 * rot % mod
                offset = s << (h - len_)
                for i in range(p):
                    a0 = a[i + offset]
                    a1 = a[i + offset + p] * rot
                    a2 = a[i + offset + p * 2] * rot2
                    a3 = a[i + offset + p * 3] * rot3
                    a1na3imag = (a1 - a3) % mod * imag
                    a[i + offset] = (a0 + a2 + a1 + a3) % mod
                    a[i + offset + p] = (a0 + a2 - a1 - a3) % mod
                    a[i + offset + p * 2] = (a0 - a2 + a1na3imag) % mod
                    a[i + offset + p * 3] = (a0 - a2 - a1na3imag) % mod
                if s + 1 != 1 << len_:
                    rot *= rate3[(~s & -~s).bit_length() - 1]
                    rot %= mod
            len_ += 2

def butterfly_inv(a):
    n = len(a)
    h = (n - 1).bit_length()
    len_ = h
    while len_:
        if len_ == 1:
            p = 1 << (h - len_)
            irot = 1
            for s in range(1 << (len_ - 1)):
                offset = s << (h - len_ + 1)
                for i in range(p):
                    l = a[i + offset]
                    r = a[i + offset + p]
                    a[i + offset] = (l + r) % mod
                    a[i + offset + p] = (l - r) * irot % mod
                if s + 1 != (1 << (len_ - 1)):
                    irot *= irate2[(~s & -~s).bit_length() - 1]
                    irot %= mod
            len_ -= 1
        else:
            p = 1 << (h - len_)
            irot = 1
            for s in range(1 << (len_ - 2)):
                irot2 = irot * irot % mod
                irot3 = irot2 * irot % mod
                offset = s << (h - len_ + 2)
                for i in range(p):
                    a0 = a[i + offset]
                    a1 = a[i + offset + p]
                    a2 = a[i + offset + p * 2]
                    a3 = a[i + offset + p * 3]
                    a2na3iimag = (a2 - a3) * iimag % mod
                    a[i + offset] = (a0 + a1 + a2 + a3) % mod
                    a[i + offset + p] = (a0 - a1 + a2na3iimag) * irot % mod
                    a[i + offset + p * 2] = (a0 + a1 - a2 - a3) * irot2 % mod
                    a[i + offset + p * 3] = (a0 - a1 - a2na3iimag) * irot3 % mod
                if s + 1 != (1 << (len_ - 2)):
                    irot *= irate3[(~s & -~s).bit_length() - 1]
                    irot %= mod
            len_ -= 2

def integrate(a):
    a=a.copy()
    n = len(a)
    assert n > 0
    a.pop()
    a.insert(0, 0)
    inv = [1, 1]
    for i in range(2, n):
        inv.append(-inv[mod%i] * (mod//i) % mod)
        a[i] = a[i] * inv[i] % mod
    return a

def differentiate(a):
    n = len(a)
    assert n > 0
    for i in range(2, n):
        a[i] = a[i] * i % mod
    a.pop(0)
    a.append(0)
    return a

def convolution_naive(a, b):
    n = len(a)
    m = len(b)
    ans = [0] * (n + m - 1)
    if n < m:
        for j in range(m):
            for i in range(n):
                ans[i + j] = (ans[i + j] + a[i] * b[j]) % mod
    else:
        for i in range(n):
            for j in range(m):
                ans[i + j] = (ans[i + j] + a[i] * b[j]) % mod
    return ans

def convolution_ntt(a, b):
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
        a[i] = a[i] * b[i] % mod
    butterfly_inv(a)
    a = a[:n + m - 1]
    iz = pow(z, mod - 2, mod)
    for i in range(n + m - 1):
        a[i] = a[i] * iz % mod
    return a

def convolution_square(a):
    a = a.copy()
    n = len(a)
    z = 1 << (2 * n - 2).bit_length()
    a += [0] * (z - n)
    butterfly(a)
    for i in range(z):
        a[i] = a[i] * a[i] % mod
    butterfly_inv(a)
    a = a[:2 * n - 1]
    iz = pow(z, mod - 2, mod)
    for i in range(2 * n - 1):
        a[i] = a[i] * iz % mod
    return a

def convolution(a, b):
    """It calculates (+, x) convolution in mod 998244353. 
    Given two arrays a[0], a[1], ..., a[n - 1] and b[0], b[1], ..., b[m - 1], 
    it calculates the array c of length n + m - 1, defined by

    >   c[i] = sum(a[j] * b[i - j] for j in range(i + 1)) % 998244353.

    It returns an empty list if at least one of a and b are empty.

    Complexity
    ----------

    >   O(n log n), where n = len(a) + len(b).
    """
    n = len(a)
    m = len(b)
    if n == 0 or m == 0:
        return []
    if min(n, m) <= 60:
        return convolution_naive(a, b)
    if a is b:
        return convolution_square(a)
    return convolution_ntt(a, b)

def inverse(a):
    n = len(a)
    assert n > 0 and a[0] != 0
    res = [pow(a[0], mod - 2, mod)]
    m = 1
    while m < n:
        f = a[:min(n,2*m)] + [0]*(2*m-min(n,2*m))
        g = res + [0]*m
        butterfly(f)
        butterfly(g)
        for i in range(2*m):
            f[i] = f[i] * g[i] % mod
        butterfly_inv(f)
        f = f[m:] + [0]*m
        butterfly(f)
        for i in range(2*m):
            f[i] = f[i] * g[i] % mod
        butterfly_inv(f)
        iz = pow(2*m, mod-2, mod)
        iz = (-iz*iz) % mod
        for i in range(m):
            f[i] = f[i] * iz % mod
        res += f[:m]
        m <<= 1
    return res[:n]

def log(a):
    a = a.copy()
    n = len(a)
    assert n > 0 and a[0] == 1
    a_inv = inverse(a)
    a=differentiate(a)
    a = convolution(a, a_inv)[:n]
    a=integrate(a)
    return a

def exp(a):
    a = a.copy()
    n = len(a)
    assert n > 0 and a[0] == 0
    g = [1]
    a[0] = 1
    h_drv = a.copy()
    h_drv=differentiate(h_drv)
    m = 1
    while m < n:
        f_fft = a[:m] + [0] * m
        butterfly(f_fft)

        if m > 1:
            _f = [f_fft[i] * g_fft[i] % mod for i in range(m)]
            butterfly_inv(_f)
            _f = _f[m // 2:] + [0] * (m // 2)
            butterfly(_f)
            for i in range(m):
                _f[i] = _f[i] * g_fft[i] % mod
            butterfly_inv(_f)
            _f = _f[:m//2]
            iz = pow(m, mod - 2, mod)
            iz *= -iz
            iz %= mod
            for i in range(m//2):
                _f[i] = _f[i] * iz % mod
            g.extend(_f)

        t = a[:m]
        t=differentiate(t)
        r = h_drv[:m - 1]
        r.append(0)
        butterfly(r)
        for i in range(m):
            r[i] = r[i] * f_fft[i] % mod
        butterfly_inv(r)
        im = pow(-m, mod - 2, mod)
        for i in range(m):
            r[i] = r[i] * im % mod
        for i in range(m):
            t[i] = (t[i] + r[i]) % mod
        t = [t[-1]] + t[:-1]

        t += [0] * m
        butterfly(t)
        g_fft = g + [0] * (2 * m - len(g))
        butterfly(g_fft)
        for i in range(2 * m):
            t[i] = t[i] * g_fft[i] % mod
        butterfly_inv(t)
        t = t[:m]
        i2m = pow(2 * m, mod - 2, mod)
        for i in range(m):
            t[i] = t[i] * i2m % mod
    
        v = a[m:min(n, 2 * m)]
        v += [0] * (m - len(v))
        t = [0] * (m - 1) + t + [0]
        t=integrate(t)
        for i in range(m):
            v[i] = (v[i] - t[m + i]) % mod

        v += [0] * m
        butterfly(v)
        for i in range(2 * m):
            v[i] = v[i] * f_fft[i] % mod
        butterfly_inv(v)
        v = v[:m]
        i2m = pow(2 * m, mod - 2, mod)
        for i in range(m):
            v[i] = v[i] * i2m % mod
        
        for i in range(min(n - m, m)):
            a[m + i] = v[i]
        
        m *= 2
    return a

def power(a,k):
    n = len(a)
    assert n>0
    if k==0:
        return [1]+[0]*(n-1)
    l = 0
    while l < len(a) and not a[l]:
        l += 1
    if l * k >= n:
        return [0] * n
    ic = pow(a[l], mod - 2, mod)
    pc = pow(a[l], k, mod)
    a = log([a[i] * ic % mod for i in range(l, len(a))])
    for i in range(len(a)):
        a[i] = a[i] * k % mod
    a = exp(a)
    for i in range(len(a)):
        a[i] = a[i] * pc % mod
    a = [0] * (l * k) + a[:n - l * k]
    return a
    


N,M=map(int,readline().split())
pol = [1, 1] + [0] * (N - 1)
print(*power(pol, N))


# print(len(binary_exp_fft_conv(pol, n)))