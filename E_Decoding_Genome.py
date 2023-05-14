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
# from copy import deepcopy

# transpose = lambda mat: [list(col) for col in zip(*mat)]

# minor = lambda mat, i, j: [row[:j] + row[j + 1:] for row in (mat[:i] + mat[i + 1:])]

# mat_add = lambda *mat: [[sum(elements) for elements in zip(*row)] for row in zip(*mat)]

# mat_sub = lambda A, B: [[i - j for i, j in zip(*row)] for row in zip(A, B)]

# _mat_mul = lambda A, B: [[sum((i * j) % M for i, j in zip(row, col)) % M for col in zip(*B)] for row in A]
# def mat_mul(A, B):
#     ans = []
#     for row in A:
#         ans.append([0] * len(B[0]))
#         for i, j in enumerate(row):
#             for k, l in enumerate(B[i]):
#                 ans[-1][k] += j * l
#                 ans[-1][k] %= M

#     return ans

# vec_mul = lambda mat, vec: [sum(a * b for a, b in zip(row, vec)) for row in mat]


# def eye(m):
#     """returns an indentity matrix of order m"""
#     identity = [[0] * m for _ in range(m)]
#     for i, row in enumerate(identity):
#         row[i] = 1
#     return identity


# def mat_pow(mat, power):
#     """returns mat**power"""
#     if power < 0:
#         return mat_pow(mat_inv(mat), -power)

#     result = eye(len(mat))
#     if power == 0:
#         return result

#     while power > 1:
#         if power & 1 == 1:
#             result = mat_mul(result, mat)
#         mat = mat_mul(mat, mat)
#         power >>= 1
#     return mat_mul(result, mat)


# def mat_inv(A):
#     B = deepcopy(A)
#     n = len(A)
#     col = list(range(n))

#     tmp = [[0] * n for _ in range(n)]
#     for i in range(n):
#         tmp[i][i] = 1

#     for i in range(n):
#         r = c = i
#         for j in range(i, n):
#             for k in range(i, n):
#                 if abs(B[j][k]) > abs(B[r][c]):
#                     r, c = j, k
#         if B[r][c] == 0:
#             return B

#         B[i], B[r] = B[r], B[i]
#         tmp[i], tmp[r] = tmp[r], tmp[i]
#         for j in range(n):
#             B[j][i], B[j][c] = B[j][c], B[j][i]
#             tmp[j][i], tmp[j][c] = tmp[j][c], tmp[j][i]
#         col[i], col[c] = col[c], col[i]
#         v = B[i][i]
#         for j in range(i + 1, n):
#             f = B[j][i] / v
#             B[j][i] = 0
#             for k in range(i + 1, n):
#                 B[j][k] -= f * B[i][k]
#             for k in range(n):
#                 tmp[j][k] -= f * tmp[i][k]

#         for j in range(i + 1, n):
#             B[i][j] /= v

#         for j in range(n):
#             tmp[i][j] /= v
#         B[i][i] = 1

#     for i in reversed(range(n)):
#         for j in range(i):
#             v = B[j][i]
#             for k in range(n):
#                 tmp[j][k] -= v * tmp[i][k]

#     for i in range(n):
#         for j in range(n):
#             B[col[i]][col[j]] = tmp[i][j]
#     return B

MOD = 1000000007

class Matrix():
    def __init__(self, n, m, mat=None):
        self.n = n
        self.m = m
        self.mat = [[0] * self.m for _ in range(self.n)]
        if mat:
            assert len(mat) == n and len(mat[0]) == m
            for i in range(self.n):
                self.mat[i] = mat[i].copy()

    def is_square(self):
        return self.n == self.m

    def __getitem__(self, key):
        if isinstance(key, slice):
            return self.mat[key]
        else:
            assert key >= 0
            return self.mat[key]

    def id(n):
        res = Matrix(n, n)
        for i in range(n):
            res[i][i] = 1
        return res

    def __len__(self):
        return len(self.mat)

    def __str__(self):
        return '\n'.join(' '.join(map(str, self[i])) for i in range(self.n))

    def times(self, k):
        res = [[0] * self.m for _ in range(self.n)]
        for i in range(self.n):
            res_i, self_i = res[i], self[i]
            for j in range(self.m):
                res_i[j] = k * self_i[j] % MOD
        return Matrix(self.n, self.m, res)

    def __pos__(self):
        return self

    def __neg__(self):
        return self.times(-1)

    def __add__(self, other):
        assert self.n == other.n and self.m == other.m
        res = [[0] * self.m for _ in range(self.n)]
        for i in range(self.n):
            res_i, self_i, other_i = res[i], self[i], other[i]
            for j in range(self.m):
                res_i[j] = (self_i[j] + other_i[j]) % MOD
        return Matrix(self.n, self.m, res)

    def __sub__(self, other):
        assert self.n == other.n and self.m == other.m
        res = [[0] * self.m for _ in range(self.n)]
        for i in range(self.n):
            res_i, self_i, other_i = res[i], self[i], other[i]
            for j in range(self.m):
                res_i[j] = (self_i[j] - other_i[j]) % MOD
        return Matrix(self.n, self.m, res)

    def __mul__(self, other):
        if other.__class__ == Matrix:
            assert self.m == other.n
            res = [[0] * other.m for _ in range(self.n)]
            for i in range(self.n):
                res_i, self_i = res[i], self[i]
                for k in range(self.m):
                    self_ik, other_k = self_i[k], other[k]
                    for j in range(other.m):
                        res_i[j] += self_ik * other_k[j]
                        res_i[j] %= MOD
            return Matrix(self.n, other.m, res)
        else:
            return self.times(other)

    def __rmul__(self, other):
        return self.times(other)

    def __pow__(self, k):
        assert self.is_square()
        tmp = Matrix(self.n, self.n, self.mat)
        res = Matrix.id(self.n)
        while k:
            if k & 1:
                res *= tmp
            tmp *= tmp
            k >>= 1
        return res

# import sys
# input = sys.stdin.buffer.readline

# N, M, K = map(int, input().split())

# A = [list(map(int, input().split())) for _ in range(N)]
# B = [list(map(int, input().split())) for _ in range(M)]

# A = Matrix(N, M, A)
# B = Matrix(M, K, B)

# C = A * B

# print(C)



def main():
    TestCases = 1
    for i in range(26):
        abd[chr(i + 65)] = i + 26
    for _ in range(TestCases):
        n, m, k = [int(i) for i in input().split()]
        mat = [[1] * m for _ in range(m)]
        for i in range(k):
            s = input()
            x, y = abd[s[0]], abd[s[1]]
            mat[x][y] = 0
        mat = Matrix(m, m, mat)
        mat = pow(mat, n-1)
        # print(mat)
        # mat = mat_pow(mat, n-1)
        ans = 0
        for row in mat:
            ans += sum(row)
            ans %= M
            # for i in row:
            #     ans += i
            #     if ans >= M:
            #         ans -= M
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
