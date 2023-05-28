# https://atcoder.jp/contests/practice2/submissions/24534749

import sys
input = lambda : sys.stdin.readline().rstrip()
write = lambda x: sys.stdout.write(x+"\n")



class LSG:
    def __init__(self,n, a=None):
        self._n = n
        self._ninf = ninf
        x = 0
        while (1 << x) < self._n:
            x += 1
        self._log = x
        self._size = 1 << self._log
        self._d = [ninf] * (2 * self._size)
        self._lz = [f0] * self._size
        if a is not None:
            for i in range(self._n):
                self._d[self._size + i] = a[i]
            for i in range(self._size - 1, 0, -1):
                self._update(i)
    def check(self):
        return [self.query_point(p) for p in range(self._n)]
    def update_point(self, p, x):
        p += self._size
        for i in range(self._log, 0, -1):
            self._push(p >> i)
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)
    def query_point(self, p):
        p += self._size
        for i in range(self._log, 0, -1):
            self._push(p >> i)
        return self._d[p]
    def query(self, left, right):
        if left == right:
            return ninf
        left += self._size
        right += self._size
        for i in range(self._log, 0, -1):
            if ((left >> i) << i) != left:
                self._push(left >> i)
            if ((right >> i) << i) != right:
                self._push(right >> i)
        sml = ninf
        smr = ninf
        while left < right:
            if left & 1:
                sml = op(sml, self._d[left])
                left += 1
            if right & 1:
                right -= 1
                smr = op(self._d[right], smr)
            left >>= 1
            right >>= 1
        return op(sml, smr)
    def query_all(self):
        return self._d[1]
    def update(self, left, right, f):
        if right is None:
            p = left
            p += self._size
            for i in range(self._log, 0, -1):
                self._push(p >> i)
            self._d[p] = mapping(f, self._d[p])
            for i in range(1, self._log + 1):
                self._update(p >> i)
        else:
            if left == right:
                return
            left += self._size
            right += self._size
            for i in range(self._log, 0, -1):
                if ((left >> i) << i) != left:
                    self._push(left >> i)
                if ((right >> i) << i) != right:
                    self._push((right - 1) >> i)
            l2 = left
            r2 = right
            while left < right:
                if left & 1:
                    self._all_apply(left, f)
                    left += 1
                if right & 1:
                    right -= 1
                    self._all_apply(right, f)
                left >>= 1
                right >>= 1
            left = l2
            right = r2
            for i in range(1, self._log + 1):
                if ((left >> i) << i) != left:
                    self._update(left >> i)
                if ((right >> i) << i) != right:
                    self._update((right - 1) >> i)
    def _update(self, k):
        self._d[k] = op(self._d[2 * k], self._d[2 * k + 1])
    def _all_apply(self, k, f) -> None:
        self._d[k] = mapping(f, self._d[k])
        if k < self._size:
            self._lz[k] = composition(f, self._lz[k])
    def _push(self, k):
        self._all_apply(2 * k, self._lz[k])
        self._all_apply(2 * k + 1, self._lz[k])
        self._lz[k] = f0
    def loc(self, l, r):
        return self._lz[self._size+l : self._size+r]

n,q = list(map(int, input().split()))
a = list(map(int, input().split()))
# ninf = -10**9
# op = max
# mapping = lambda f,x: f(x)
# composition = lambda f1, f2: f1 if f1 is not None else f2
M = 998244353
ninf = 0
B = 32
f0 = 1<<B
mask = (1<<B)-1
def op(x,y):
    x0,x1 = x>>B, x&mask
    y0,y1 = y>>B, y&mask
    return (((x0+y0)%M)<<B) + x1+y1
def mapping(f,x):
    x0,x1 = x>>B, x&mask
    f0,f1 = f>>B, f&mask
    return (((f0*x0 + f1*x1)%M)<<B) + x1
def composition(f,g):
    g0,g1 = g>>B, g&mask
    f0,f1 = f>>B, f&mask
    return (((f0*g0)%M)<<B) + (g1*f0 + f1)%M
# op = lambda x,y: ((x[0]+y[0])%M, (x[1]+y[1]))
# mapping = lambda f,x: ((f[0]*x[0] + f[1]*x[1])%M, x[1])
# composition = lambda f1, f2: ((f1[0]*f2[0])%M, (f2[1]*f1[0]+f1[1])%M)
# f0 = (1,0)
sg = LSG(n, [((item<<B)+1) for item in a])
ans = []
for _ in range(q):
    t = tuple(map(int, input().split()))
    if t[0]==0:
        _, l,r,b,c = t
        sg.update(l,r,f=((b<<B)+c))
    else:
        _,s,t = t
        ans.append(sg.query(s,t)>>B)
        
write("\n".join(map(str, ans)))
