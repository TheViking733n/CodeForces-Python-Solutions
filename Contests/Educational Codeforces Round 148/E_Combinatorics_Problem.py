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


# INF = float("inf")
INF = 9223372036854775807
PI = 3.141592653589793
R = randrange(2, 1 << 32)
# R = 0          # Enable this for debugging of dict keys in myDict

# ========================= Main ==========================

MOD=M=998244353
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



## ==========================================
# import sys
# readline=sys.stdin.readline
# class FPS:
#     sum_e = (
#     911660635, 509520358, 369330050, 332049552, 983190778, 123842337, 238493703, 975955924, 603855026, 856644456,
#     131300601, 842657263, 730768835, 942482514, 806263778, 151565301, 510815449, 503497456, 743006876, 741047443,
#     56250497)
#     sum_ie = (
#     86583718, 372528824, 373294451, 645684063, 112220581, 692852209, 155456985, 797128860, 90816748, 860285882,
#     927414960, 354738543, 109331171, 293255632, 535113200, 308540755, 121186627, 608385704, 438932459, 359477183,
#     824071951)
#     mod = 998244353
#     Func = [0]

#     def __init__(self, L):
#         self.Func = [x % self.mod for x in L]

#     def butterfly(self, a):
#         n = len(a)
#         h = (n - 1).bit_length()
#         for ph in range(1, h + 1):
#             w = 1 << (ph - 1)
#             p = 1 << (h - ph)
#             now = 1
#             for s in range(w):
#                 offset = s << (h - ph + 1)
#                 for i in range(p):
#                     l = a[i + offset]
#                     r = a[i + offset + p] * now
#                     r %= self.mod
#                     a[i + offset] = l + r
#                     a[i + offset] %= self.mod
#                     a[i + offset + p] = l - r
#                     a[i + offset + p] %= self.mod
#                 now *= self.sum_e[(~s & -~s).bit_length() - 1]
#                 now %= self.mod
#         return a

#     def butterfly_inv(self, a):
#         n = len(a)
#         h = (n - 1).bit_length()
#         for ph in range(h, 0, -1):
#             w = 1 << (ph - 1)
#             p = 1 << (h - ph)
#             inow = 1
#             for s in range(w):
#                 offset = s << (h - ph + 1)
#                 for i in range(p):
#                     l = a[i + offset]
#                     r = a[i + offset + p]
#                     a[i + offset] = l + r
#                     a[i + offset] %= self.mod
#                     a[i + offset + p] = (l - r) * inow
#                     a[i + offset + p] %= self.mod
#                 inow *= self.sum_ie[(~s & -~s).bit_length() - 1]
#                 inow %= self.mod
#         return a

#     def __mul__(self, other):
#         if type(other) == int:
#             ret = [(x * other) % self.mod for x in self.Func]
#             return FPS(ret)
#         a = self.Func
#         b = other.Func
#         n = len(a);
#         m = len(b)
#         if not (a) or not (b):
#             return FPS([])
#         if min(n, m) <= 40:
#             if n < m:
#                 n, m = m, n
#                 a, b = b, a
#             res = [0] * (n + m - 1)
#             for i in range(n):
#                 for j in range(m):
#                     res[i + j] += a[i] * b[j]
#                     res[i + j] %= self.mod
#             return FPS(res)
#         z = 1 << ((n + m - 2).bit_length())
#         a = a + [0] * (z - n)
#         b = b + [0] * (z - m)
#         a = self.butterfly(a)
#         b = self.butterfly(b)
#         c = [0] * z
#         for i in range(z):
#             c[i] = (a[i] * b[i]) % self.mod
#         self.butterfly_inv(c)
#         iz = pow(z, self.mod - 2, self.mod)
#         for i in range(n + m - 1):
#             c[i] = (c[i] * iz) % self.mod
#         return FPS(c[:n + m - 1])

#     def __imul__(self, other):
#         self = self * other
#         return self

#     def __add__(self, other):
#         res = [0 for i in range(max(len(self.Func), len(other.Func)))]
#         for i, x in enumerate(self.Func):
#             res[i] += x
#             res[i] %= self.mod
#         for i, x in enumerate(other.Func):
#             res[i] += x
#             res[i] %= self.mod
#         return FPS(res)

#     def __iadd__(self, other):
#         self = (self + other)
#         return self

#     def __sub__(self, other):
#         res = [0 for i in range(max(len(self.Func), len(other.Func)))]
#         for i, x in enumerate(self.Func):
#             res[i] += x
#             res[i] %= self.mod
#         for i, x in enumerate(other.Func):
#             res[i] -= x
#             res[i] %= self.mod
#         return FPS(res)

#     def __isub__(self, other):
#         self = self - other
#         return self

#     def inv(self, d=-1):
#         n = len(self.Func)
#         assert n != 0 and self.Func[0] != 0
#         if d == -1: d = n
#         assert d > 0
#         res = [pow(self.Func[0], self.mod - 2, self.mod)]
#         while (len(res) < d):
#             m = len(res)
#             f = [self.Func[i] for i in range(min(n, 2 * m))]
#             r = res[:]

#             if len(f) < 2 * m:
#                 f += [0] * (2 * m - len(f))
#             elif len(f) > 2 * m:
#                 f = f[:2 * m]
#             if len(r) < 2 * m:
#                 r += [0] * (2 * m - len(r))
#             elif len(r) > 2 * m:
#                 r = r[:2 * m]
#             f = self.butterfly(f)
#             r = self.butterfly(r)
#             for i in range(2 * m):
#                 f[i] *= r[i]
#                 f[i] %= self.mod
#             f = self.butterfly_inv(f)
#             f = f[m:]
#             if len(f) < 2 * m:
#                 f += [0] * (2 * m - len(f))
#             elif len(f) > 2 * m:
#                 f = f[:2 * m]
#             f = self.butterfly(f)
#             for i in range(2 * m):
#                 f[i] *= r[i]
#                 f[i] %= self.mod
#             f = self.butterfly_inv(f)
#             iz = pow(2 * m, self.mod - 2, self.mod)
#             iz *= -iz
#             iz %= self.mod
#             for i in range(m):
#                 f[i] *= iz
#                 f[i] %= self.mod
#             res += f[:m]
#         return FPS(res[:d])

#     def __truediv__(self, other):
#         if type(other) == int:
#             invother = pow(other, self.mod - 2, self.mod)
#             ret = [(x * invother) % self.mod for x in self.Func]
#             return FPS(ret)
#         assert (other.Func[0] != 0)
#         return self * (other.inv())

#     def __itruediv__(self, other):
#         self = self / other
#         return self

#     def __lshift__(self, d):
#         n = len(self.Func)
#         self.Func = [0] * d + self.Func
#         return FPS(self.Func[:n])

#     def __ilshift__(self, d):
#         self = self << d
#         return self

#     def __rshift__(self, d):
#         n = len(self.Func)
#         self.Func = self.Func[min(n, d):]
#         self.Func += [0] * (n - len(self.Func))
#         return FPS(self.Func)

#     def __irshift__(self, d):
#         self = self >> d
#         return self

#     def __str__(self):
#         return f'FPS({self.Func})'

#     def diff(self):
#         n = len(self.Func)
#         ret = [0 for i in range(max(0, n - 1))]
#         for i in range(1, n):
#             ret[i - 1] = (self.Func[i] * i) % self.mod
#         return FPS(ret)

#     def integral(self):
#         n = len(self.Func)
#         ret = [0 for i in range(n + 1)]
#         for i in range(n):
#             ret[i + 1] = self.Func[i] * pow(i + 1, self.mod - 2, self.mod) % self.mod
#         return FPS(ret)

#     def log(self, deg=-1):
#         assert self.Func[0] == 1
#         n = len(self.Func)
#         if deg == -1: deg = n
#         return (self.diff() * self.inv()).integral()

#     def mod_sqrt(self, a):
#         p = self.mod
#         assert 0 <= a and a < p
#         if a < 2: return a
#         if pow(a, (p - 1) // 2, p) != 1: return -1
#         b = 1;
#         one = 1
#         while (pow(b, (p - 1) >> 1, p) == 1):
#             b += one
#         m = p - 1;
#         e = 0
#         while (m % 2 == 0):
#             m >>= 1
#             e += 1
#         x = pow(a, (m - 1) >> 1, p)
#         y = (a * x * x) % p
#         x *= a;
#         x %= p
#         z = pow(b, m, p)
#         while (y != 1):
#             j = 0
#             t = y
#             while (t != one):
#                 j += 1
#                 t *= t
#                 t %= p
#             z = pow(z, 1 << (e - j - 1), p)
#             x *= z
#             x %= p
#             z *= z
#             z %= p
#             y *= z
#             y %= p
#             e = j
#         return x

#     def sqrt(self, deg=-1):
#         n = len(self.Func)
#         if deg == -1: deg = n
#         if n == 0: return FPS([0 for i in range(deg)])
#         if self.Func[0] == 0:
#             for i in range(1, n):
#                 if self.Func[i] != 0:
#                     if i & 1: return FPS([])
#                     if deg - i // 2 <= 0: break
#                     ret = (self >> i).sqrt(deg - i // 2)
#                     if len(ret.Func) == 0: return FPS([])
#                     ret = ret << (i // 2)
#                     if len(ret.Func) < deg:
#                         ret.Func += [0] * (deg - len(ret.Func))
#                     return ret
#             return FPS([0] * deg)
#         sqr = self.mod_sqrt(self.Func[0])
#         if sqr == -1: return FPS([])
#         assert sqr * sqr % self.mod == self.Func[0]
#         ret = FPS([sqr])
#         inv2 = (self.mod + 1) // 2
#         i = 1
#         while (i < deg):
#             ret = (ret + FPS(self.Func[:i << 1]) * ret.inv(i << 1)) * inv2
#             i <<= 1
#         return FPS(ret.Func[:deg])

#     def resize(self, deg):
#         if len(self.Func) < deg:
#             return FPS(self.Func + [0] * (deg - len(self.Func)))
#         elif len(self.Func) > deg:
#             return FPS(self.Func[:deg])
#         else:
#             return self

#     def exp(self, deg=-1):
#         n = len(self.Func)
#         assert n > 0 and self.Func[0] == 0
#         if deg == -1: deg = n
#         assert deg >= 0
#         g = [1]
#         g_fft = [1, 1]
#         self.Func[0] = 1
#         self.resize(deg)
#         h_drv = self.diff()
#         m = 2
#         while (m < deg):
#             f_fft = self.Func[:m] + [0] * m
#             self.butterfly(f_fft)

#             # step 2.a
#             _g = [f_fft[i] * g_fft[i] % self.mod for i in range(m)]
#             self.butterfly_inv(_g)
#             _g = _g[m // 2:m] + [0] * (m // 2)
#             self.butterfly(_g)
#             for i in range(m):
#                 _g[i] *= g_fft[i]
#                 _g[i] %= self.mod
#             self.butterfly_inv(_g)
#             tmp = pow(-m * m, self.mod - 2, self.mod)
#             for i in range(m):
#                 _g[i] *= tmp
#                 _g[i] %= self.mod
#             g += _g[:m // 2]
#             # step 2.b--2.d
#             t = FPS(self.Func[:m]).diff()
#             r = h_drv.Func[:m - 1] + [0]
#             self.butterfly(r)
#             for i in range(m):
#                 r[i] *= f_fft[i]
#                 r[i] %= self.mod
#             self.butterfly_inv(r)
#             tmp = pow(-m, self.mod - 2, self.mod)
#             for i in range(m):
#                 r[i] *= tmp
#                 r[i] %= self.mod
#             t = (t + FPS(r)).Func
#             t = [t[-1]] + t
#             t.pop()
#             # step 2.e
#             if (2 * m < deg):
#                 if len(t) < 2 * m:
#                     t += [0] * (2 * m - len(t))
#                 elif len(t) > 2 * m:
#                     t = t[:2 * m]
#                 self.butterfly(t)
#                 g_fft = g[:]
#                 if len(g_fft) < 2 * m:
#                     g_fft += [0] * (2 * m - len(g_fft))
#                 elif len(g_fft) > 2 * m:
#                     g_fft = g_fft[:2 * m]
#                 self.butterfly(g_fft)
#                 for i in range(2 * m):
#                     t[i] *= g_fft[i]
#                     t[i] %= self.mod
#                 self.butterfly_inv(t)
#                 tmp = pow(2 * m, self.mod - 2, self.mod)
#                 t = t[:m]
#                 for i in range(m):
#                     t[i] *= tmp
#                     t[i] %= self.mod
#             else:
#                 g1 = g[m // 2:]
#                 s1 = t[m // 2:]
#                 t = t[:m // 2]
#                 g1 += [0] * (m - len(g1))
#                 s1 += [0] * (m - len(s1))
#                 t += [0] * (m - len(t))

#                 self.butterfly(g1)
#                 self.butterfly(t)
#                 self.butterfly(s1)
#                 for i in range(m):
#                     s1[i] = (g_fft[i] * s1[i] + g1[i] * t[i]) % self.mod
#                 for i in range(m):
#                     t[i] *= g_fft[i]
#                     t[i] %= self.mod
#                 self.butterfly_inv(t)
#                 self.butterfly_inv(s1)
#                 for i in range(m // 2):
#                     t[i + m // 2] += s1[i]
#                     t[i + m // 2] %= self.mod
#                 tmp = pow(m, self.mod - 2, self.mod)
#                 for i in range(m):
#                     t[i] *= tmp
#                     t[i] %= self.mod
#             # step 2.f
#             v = self.Func[m:min(deg, 2 * m)] + [0] * (2 * m - min(deg, 2 * m))
#             t = [0] * (m - 1) + t
#             t = FPS(t).integral().Func
#             for i in range(m):
#                 v[i] -= t[m + i]
#                 v[i] %= self.mod
#             # step 2.g
#             if len(v) < 2 * m:
#                 v += [0] * (2 * m - len(v))
#             else:
#                 v = v[:2 * m]
#             self.butterfly(v)
#             for i in range(2 * m):
#                 v[i] *= f_fft[i]
#                 v[i] %= self.mod
#             self.butterfly_inv(v)
#             v = v[:m]
#             tmp = pow(2 * m, self.mod - 2, self.mod)
#             for i in range(m):
#                 v[i] *= tmp
#                 v[i] %= self.mod
#             # step 2.h
#             for i in range(min(deg - m, m)):
#                 self.Func[m + i] = v[i]
#             m *= 2
#         return self

#     def powfps(self, k, deg=-1):
#         a = self.Func[:]
#         n = len(self.Func)
#         l = 0
#         while (l < len(a) and not a[l]):
#             l += 1
#         if l * k >= n:
#             return FPS([0] * n)
#         ic = pow(a[l], self.mod - 2, self.mod)
#         pc = pow(a[l], k, self.mod)
#         a = FPS([(a[i] * ic) % self.mod for i in range(l, len(a))]).log()
#         a *= k
#         a = a.exp()
#         a *= pc
#         a = [0] * (l * k) + a.Func[:n - l * k]
#         return FPS(a)


# =============================================================================


# MOD = 998244353
# OMEGA = 3

# def power(b, e):
#     r = 1
#     if e & 1:
#         r = b
#     while e:
#         e >>= 1
#         b = (b * b) % MOD
#         if e & 1: r = (r * b) % MOD
#     return r

# def ntt(a, inv=False):
#     n = len(a)
#     rev = [0] * n
#     for i in range(n):
#         rev[i] = rev[i >> 1] >> 1
#         if i & 1:
#             rev[i] |= n >> 1
#         if i < rev[i]:
#             a[i], a[rev[i]] = a[rev[i]], a[i]

#     ang = power(OMEGA, (MOD - 1) // n)
#     if inv:
#         ang = power(ang, MOD - 2);
#     w = [0] * (n >> 1)
#     w[0] = 1
#     for i in range(1, n >> 1):
#         w[i] = w[i-1] * ang % MOD
    
#     step = 2
#     while step <= n:
#         half, diff = step >> 1, n // step
#         for i in range(0, n, step):
#             pw = 0
#             for j in range(i, i + half):
#                 v = a[j + half] * w[pw] % MOD
#                 a[j + half] = (a[j] - v) % MOD
#                 a[j] = (a[j] + v) % MOD
#                 pw = (pw + diff) % MOD
#         step <<= 1

#     t = power(n, MOD - 2)
#     if inv:
#         for i in range(n):
#             a[i] = a[i] * t % MOD


# def ntt_conv(a, b):
#     s = len(a) + len(b) - 1
#     n = 1 << s.bit_length()
#     a.extend([0] * (n - len(a)))
#     b.extend([0] * (n - len(b)))

#     ntt(a), ntt(b)
#     for i in range(n):
#         a[i] = a[i] * b[i] % MOD
#     ntt(a, True)
#     return a






#============================================================================
# import sys
# # sys.setrecursionlimit(5 * 10 ** 5)
# # from pypyjit import set_param
# # set_param('max_unroll_recursion=-1')
# input = lambda: sys.stdin.readline().rstrip()
# ii = lambda: int(input())
# mi = lambda: map(int, input().split())
# li = lambda: list(mi())
# inf = 2 ** 63 - 1
# mod = 998244353
# """
# Reference
# https://github.com/atcoder/ac-library/blob/master/atcoder/convolution.hpp
# https://github.com/atcoder/ac-library/blob/master/atcoder/internal_math.hpp
# https://github.com/atcoder/ac-library/blob/master/document_en/convolution.md
# https://github.com/atcoder/ac-library/blob/master/document_ja/convolution.md
# """
# mod = 998244353
# def primitive_root(m):
#     if m == 2:
#         return 1
#     if m == 167772161:
#         return 3
#     if m == 469762049:
#         return 3
#     if m == 754974721:
#         return 11
#     if m == 998244353:
#         return 3
#     divs = [0] * 20
#     divs[0] = 2
#     cnt = 1
#     x = (m - 1) // 2
#     while x % 2 == 0:
#         x //= 2
#     i = 3
#     while i * i <= x:
#         if x % i == 0:
#             divs[cnt] = i
#             cnt += 1
#             while x % i == 0:
#                 x //= i
#         i += 2
#     if x > 1:
#         divs[cnt] = x
#         cnt += 1
#     g = 2
#     while True:
#         ok = True
#         for i in range(cnt):
#             if pow(g, (m - 1) // divs[i], m) == 1:
#                 ok = False
#                 break
#         if ok:
#             return g
#         g += 1
 
 
# class FFT_INFO:
#     def __init__(self):
#         self.g = primitive_root(mod)
#         self.rank2 = ((mod - 1) & (1 - mod)).bit_length() - 1
#         self.root = [0] * (self.rank2 + 1)
#         self.root[self.rank2] = pow(self.g, (mod - 1) >> self.rank2, mod)
#         self.iroot = [0] * (self.rank2 + 1)
#         self.iroot[self.rank2] = pow(self.root[self.rank2], mod - 2, mod)
#         for i in range(self.rank2 - 1, -1, -1):
#             self.root[i] = self.root[i + 1] * self.root[i + 1] % mod
#             self.iroot[i] = self.iroot[i + 1] * self.iroot[i + 1] % mod
 
#         self.rate2 = [0] * max(0, self.rank2 - 1)
#         self.irate2 = [0] * max(0, self.rank2 - 1)
#         prod = 1
#         iprod = 1
#         for i in range(self.rank2 - 1):
#             self.rate2[i] = self.root[i + 2] * prod % mod
#             self.irate2[i] = self.iroot[i + 2] * iprod % mod
#             prod *= self.iroot[i + 2]
#             prod %= mod
#             iprod *= self.root[i + 2]
#             iprod %= mod
 
#         self.rate3 = [0] * max(0, self.rank2 - 2)
#         self.irate3 = [0] * max(0, self.rank2 - 2)
#         prod = 1
#         iprod = 1
#         for i in range(self.rank2 - 2):
#             self.rate3[i] = self.root[i + 3] * prod % mod
#             self.irate3[i] = self.iroot[i + 3] * iprod % mod
#             prod *= self.iroot[i + 3]
#             prod %= mod
#             iprod *= self.root[i + 3]
#             iprod %= mod
 
 
# info = FFT_INFO()
 
 
# def butterfly(a):
#     n = len(a)
#     h = (n - 1).bit_length()
 
#     length = 0
#     while length < h:
#         if h - length == 1:
#             p = 1 << (h - length - 1)
#             rot = 1
#             for s in range(1 << length):
#                 offset = s << (h - length)
#                 for i in range(p):
#                     l = a[i + offset]
#                     r = a[i + offset + p] * rot % mod
#                     a[i + offset] = (l + r) % mod
#                     a[i + offset + p] = (l - r) % mod
#                 if s + 1 != (1 << length):
#                     rot *= info.rate2[(~s & -~s).bit_length() - 1]
#                     rot %= mod
#             length += 1
#         else:
#             # 4-base
#             p = 1 << (h - length - 2)
#             rot = 1
#             imag = info.root[2]
#             for s in range(1 << length):
#                 rot2 = rot * rot % mod
#                 rot3 = rot2 * rot % mod
#                 offset = s << (h - length)
#                 for i in range(p):
#                     a0 = a[i + offset]
#                     a1 = a[i + offset + p] * rot
#                     a2 = a[i + offset + 2 * p] * rot2
#                     a3 = a[i + offset + 3 * p] * rot3
#                     a1na3imag = (a1 - a3) % mod * imag
#                     a[i + offset] = (a0 + a2 + a1 + a3) % mod
#                     a[i + offset + p] = (a0 + a2 - a1 - a3) % mod
#                     a[i + offset + 2 * p] = (a0 - a2 + a1na3imag) % mod
#                     a[i + offset + 3 * p] = (a0 - a2 - a1na3imag) % mod
#                 if s + 1 != (1 << length):
#                     rot *= info.rate3[(~s & -~s).bit_length() - 1]
#                     rot %= mod
#             length += 2
 
 
# def butterfly_inv(a):
#     n = len(a)
#     h = (n - 1).bit_length()
 
#     length = h  # a[i, i+(n<<length), i+2*(n>>length), ...] is transformed 
#     while length:
#         if length == 1:
#             p = 1 << (h - length)
#             irot = 1
#             for s in range(1 << (length - 1)):
#                 offset = s << (h - length + 1)
#                 for i in range(p):
#                     l = a[i + offset]
#                     r = a[i + offset + p]
#                     a[i + offset] = (l + r) % mod
#                     a[i + offset + p] = (l - r) * irot % mod
#                 if s + 1 != (1 << (length - 1)):
#                     irot *= info.irate2[(~s & -~s).bit_length() - 1]
#                     irot %= mod
#             length -= 1
#         else:
#             # 4-base
#             p = 1 << (h - length)
#             irot = 1
#             iimag = info.iroot[2]
#             for s in range(1 << (length - 2)):
#                 irot2 = irot * irot % mod
#                 irot3 = irot2 * irot % mod
#                 offset = s << (h - length + 2)
#                 for i in range(p):
#                     a0 = a[i + offset]
#                     a1 = a[i + offset + p]
#                     a2 = a[i + offset + 2 * p]
#                     a3 = a[i + offset + 3 * p]
#                     a2na3iimag = (a2 - a3) * iimag % mod
#                     a[i + offset] = (a0 + a1 + a2 + a3) % mod
#                     a[i + offset + p] = (a0  - a1 + a2na3iimag) * irot % mod
#                     a[i + offset + 2 * p] = (a0 + a1 - a2 - a3) * irot2 % mod
#                     a[i + offset + 3 * p] = (a0  - a1 - a2na3iimag) * irot3 % mod
#                 if s + 1 != (1 << (length - 2)):
#                     irot *= info.irate3[(~s & -~s).bit_length() - 1]
#                     irot %= mod
#             length -= 2
 
 
# def convolution_naive(a, b):
#     n = len(a)
#     m = len(b)
#     ans = [0] * (n + m - 1)
#     if n < m:
#         for j in range(m):
#             for i in range(n):
#                 ans[i + j] += a[i] * b[j]
#                 ans[i + j] %= mod
#     else:
#         for i in range(n):
#             for j in range(m):
#                 ans[i + j] += a[i] * b[j]
#                 ans[i + j] %= mod
#     return ans
 
 
# def convolution_fft(a, b):
#     a = a.copy()
#     b = b.copy()
#     n = len(a)
#     m = len(b)
#     z = 1 << (n + m - 2).bit_length()
#     a += [0] * (z - n)
#     butterfly(a)
#     b += [0] * (z - m)
#     butterfly(b)
#     for i in range(z):
#         a[i] *= b[i]
#         a[i] %= mod
#     butterfly_inv(a)
#     a = a[:n + m - 1]
#     iz = pow(z, mod - 2, mod)
#     for i in range(n + m - 1):
#         a[i] *= iz
#         a[i] %= mod
#     return a
 
 
# def convolution(a, b):
#     n = len(a)
#     m = len(b)
#     if not n or not m:
#         return []
#     if min(n, m) <= 60:
#         return convolution_naive(a, b)
#     return convolution_fft(a, b)
 
#============================================================================


class FFT():
  def primitive_root_constexpr(self,m):
      if m==2:return 1
      if m==167772161:return 3
      if m==469762049:return 3
      if m==754974721:return 11
      if m==998244353:return 3
      divs=[0]*20
      divs[0]=2
      cnt=1
      x=(m-1)//2
      while(x%2==0):x//=2
      i=3
      while(i*i<=x):
          if (x%i==0):
              divs[cnt]=i
              cnt+=1
              while(x%i==0):
                  x//=i
          i+=2
      if x>1:
          divs[cnt]=x
          cnt+=1
      g=2
      while(1):
          ok=True
          for i in range(cnt):
              if pow(g,(m-1)//divs[i],m)==1:
                  ok=False
                  break
          if ok:
              return g
          g+=1
  def bsf(self,x):
      res=0
      while(x%2==0):
          res+=1
          x//=2
      return res
  rank2=0
  root=[]
  iroot=[]
  rate2=[]
  irate2=[]
  rate3=[]
  irate3=[]
  
  def __init__(self,MOD):
      self.mod=MOD
      self.g=self.primitive_root_constexpr(self.mod)
      self.rank2=self.bsf(self.mod-1)
      self.root=[0 for i in range(self.rank2+1)]
      self.iroot=[0 for i in range(self.rank2+1)]
      self.rate2=[0 for i in range(self.rank2)]
      self.irate2=[0 for i in range(self.rank2)]
      self.rate3=[0 for i in range(self.rank2-1)]
      self.irate3=[0 for i in range(self.rank2-1)]
      self.root[self.rank2]=pow(self.g,(self.mod-1)>>self.rank2,self.mod)
      self.iroot[self.rank2]=pow(self.root[self.rank2],self.mod-2,self.mod)
      for i in range(self.rank2-1,-1,-1):
          self.root[i]=(self.root[i+1]**2)%self.mod
          self.iroot[i]=(self.iroot[i+1]**2)%self.mod
      prod=1;iprod=1
      for i in range(self.rank2-1):
          self.rate2[i]=(self.root[i+2]*prod)%self.mod
          self.irate2[i]=(self.iroot[i+2]*iprod)%self.mod
          prod=(prod*self.iroot[i+2])%self.mod
          iprod=(iprod*self.root[i+2])%self.mod
      prod=1;iprod=1
      for i in range(self.rank2-2):
          self.rate3[i]=(self.root[i+3]*prod)%self.mod
          self.irate3[i]=(self.iroot[i+3]*iprod)%self.mod
          prod=(prod*self.iroot[i+3])%self.mod
          iprod=(iprod*self.root[i+3])%self.mod
  def butterfly(self,a):
      n=len(a)
      h=(n-1).bit_length()
      
      LEN=0
      while(LEN<h):
          if (h-LEN==1):
              p=1<<(h-LEN-1)
              rot=1
              for s in range(1<<LEN):
                  offset=s<<(h-LEN)
                  for i in range(p):
                      l=a[i+offset]
                      r=a[i+offset+p]*rot
                      a[i+offset]=(l+r)%self.mod
                      a[i+offset+p]=(l-r)%self.mod
                  rot*=self.rate2[(~s & -~s).bit_length()-1]
                  rot%=self.mod
              LEN+=1
          else:
              p=1<<(h-LEN-2)
              rot=1
              imag=self.root[2]
              for s in range(1<<LEN):
                  rot2=(rot*rot)%self.mod
                  rot3=(rot2*rot)%self.mod
                  offset=s<<(h-LEN)
                  for i in range(p):
                      a0=a[i+offset]
                      a1=a[i+offset+p]*rot
                      a2=a[i+offset+2*p]*rot2
                      a3=a[i+offset+3*p]*rot3
                      a1na3imag=(a1-a3)%self.mod*imag
                      a[i+offset]=(a0+a2+a1+a3)%self.mod
                      a[i+offset+p]=(a0+a2-a1-a3)%self.mod
                      a[i+offset+2*p]=(a0-a2+a1na3imag)%self.mod
                      a[i+offset+3*p]=(a0-a2-a1na3imag)%self.mod
                  rot*=self.rate3[(~s & -~s).bit_length()-1]
                  rot%=self.mod
              LEN+=2
              
  def butterfly_inv(self,a):
      n=len(a)
      h=(n-1).bit_length()
      LEN=h
      while(LEN):
          if (LEN==1):
              p=1<<(h-LEN)
              irot=1
              for s in range(1<<(LEN-1)):
                  offset=s<<(h-LEN+1)
                  for i in range(p):
                      l=a[i+offset]
                      r=a[i+offset+p]
                      a[i+offset]=(l+r)%self.mod
                      a[i+offset+p]=(l-r)*irot%self.mod
                  irot*=self.irate2[(~s & -~s).bit_length()-1]
                  irot%=self.mod
              LEN-=1
          else:
              p=1<<(h-LEN)
              irot=1
              iimag=self.iroot[2]
              for s in range(1<<(LEN-2)):
                  irot2=(irot*irot)%self.mod
                  irot3=(irot*irot2)%self.mod
                  offset=s<<(h-LEN+2)
                  for i in range(p):
                      a0=a[i+offset]
                      a1=a[i+offset+p]
                      a2=a[i+offset+2*p]
                      a3=a[i+offset+3*p]
                      a2na3iimag=(a2-a3)*iimag%self.mod
                      a[i+offset]=(a0+a1+a2+a3)%self.mod
                      a[i+offset+p]=(a0-a1+a2na3iimag)*irot%self.mod
                      a[i+offset+2*p]=(a0+a1-a2-a3)*irot2%self.mod
                      a[i+offset+3*p]=(a0-a1-a2na3iimag)*irot3%self.mod
                  irot*=self.irate3[(~s & -~s).bit_length()-1]
                  irot%=self.mod
              LEN-=2
  def convolution(self,a,b):
      n=len(a);m=len(b)
      if not(a) or not(b):
          return []
      if min(n,m)<=40:
          res=[0]*(n+m-1)
          for i in range(n):
              for j in range(m):
                  res[i+j]+=a[i]*b[j]
                  res[i+j]%=self.mod
          return res
      z=1<<((n+m-2).bit_length())
      a=a+[0]*(z-n)
      b=b+[0]*(z-m)
      self.butterfly(a)
      self.butterfly(b)
      c=[(a[i]*b[i])%self.mod for i in range(z)]
      self.butterfly_inv(c)
      iz=pow(z,self.mod-2,self.mod)
      for i in range(n):
          c[i]=(c[i]*iz)%self.mod
      return c[:n]













def extended_gcd(a, b):
    """returns gcd(a, b), s, r s.t. a * s + b * r == gcd(a, b)"""
    s, old_s = 0, 1
    r, old_r = b, a
    while r:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
    return old_r, old_s, (old_r - old_s * a) // b if b else 0


def mod_inv(a, m=MOD):
    """returns the modular inverse of a w.r.t. to m, works when a and m are coprime"""
    g, x, _ = extended_gcd(a % m, m)
    return x % m if g == 1 else None

def main():
    TestCases = 1
    
    for _ in range(TestCases):
        n, a1, x, y, m, k = [int(i) for i in input().split()]
        a = [a1]
        for i in range(n-1):
            a.append(((a[-1]*x + y) % m) % M)
        
        # pol = [nCr(i, k) for i in range(1, n + 1)]
        pol = []

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
        
        # print(-1)
        # continue
        
        # A=FPS(a)
        # B=FPS(a)
        # a=(A*B).Func

        # ntt_conv(a, a[:])

        # a = convolution(a, a)

        # a = ntt_conv(a, a[:])
        
        CONV = FFT(M)

        a = CONV.convolution(a, a)




        # print(a)
        # print(n, len(a))
        ans = 0
        for i in range(n):
            ans ^= (a[i] % M) * (i + 1)
        
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
