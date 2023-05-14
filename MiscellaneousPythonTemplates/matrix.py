# https://judge.yosupo.jp/submission/45093

# I tried matrix exponentiation. It's runtime was equalt to that of pyrival
# But it may be useful because the code is implemented in OOPs style


MOD = 998244353

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

import sys
input = sys.stdin.buffer.readline

N, M, K = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(M)]

A = Matrix(N, M, A)
B = Matrix(M, K, B)

C = A * B

print(C)