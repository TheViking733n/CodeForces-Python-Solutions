# https://atcoder.jp/contests/practice2/submissions/40527733

class SegmentTree:
    def __init__(self, n, e, arr=None):
        self.n = n
        self.log = (n-1).bit_length()
        self.size = 1<<self.log       
        self.e = e
        self.data = [e] * (self.size<<1)
        self.len = [1] * (self.size<<1)        
        if arr: self.build(arr)
            
    def _update(self, i): self.data[i] = op(self.data[i<<1], self.data[i<<1|1])
    
    def build(self, data):
        """Builds the segment tree [Called Automatically upon __init__]. O(n)"""
        for i, a in enumerate(data, self.size): self.data[i] = a
        for i in range(self.size-1, 0, -1):
            self._update(i)
            self.len[i] = self.len[i<<1] + self.len[i<<1|1]
    
    def update(self, k, x):
        """Updates the k-th element (0-indexed) to x. O(log n)"""
        k += self.size
        self.data[k] = x
        for i in range(1, self.log+1): self._update(k>>i)
    def __setitem__(self, k, x):
        k += self.size
        self.data[k] = x
        for i in range(1, self.log+1): self._update(k>>i)
            
    def add(self, k, x):
        """Adds x to the k-th element (0-indexed). O(log n)"""
        k += self.size
        self.data[k] += x
        for i in range(1, self.log+1): self._update(k>>i)
    def __iadd__(self, k, x):
        k += self.size
        self.data[k] += x
        for i in range(1, self.log+1): self._update(k>>i)

    def get(self, k):
        """Returns the k-th element (0-indexed). O(1)"""
        return self.data[k+self.size]
    def __getitem__(self, k):
        return self.data[k+self.size]
    
    def query(self, l, r):
        """Returns op(a[l], ..., a[r-1]). O(log n)"""
        sml, smr = self.e, self.e
        l += self.size
        r += self.size
        while l < r:
            if l&1:
                sml = op(sml, self.data[l])
                l += 1
            if r&1:
                r -= 1
                smr = op(self.data[r], smr)
            l >>= 1
            r >>= 1
        return op(sml, smr)
    
    def query_all(self):
        """Returns op(a[0], ..., a[n-1]). O(1)"""
        return self.data[1]
    
    def __repr__(self) -> str:
        return f"STree({[self[i] for i in range(self.n)]})"
"""
Usage of SegmentTree(n, e, arr):
    op is a binary operation on S, e.g. op = lambda x, y: x + y
    N is the length of the array, e.g. N = 10
    e is the identity element of op, e.g. e = 0
    A is the initial array, e.g. A = [1] * N
"""
# def op(x, y):
# e = 
# seg = SegmentTree(N, e, A)


class LazySegmentTree(SegmentTree):
    def __init__(self, n, e, id_, arr=None):
        super().__init__(n, e, arr)   # builds LazySegmentTree
        self.id = id_
        self.lazy = [id_] * self.size
        
    def _all_apply(self, i, F):
        self.data[i] = mapping(F, self.data[i], self.len[i])
        if i < self.size: self.lazy[i] = composition(F, self.lazy[i])
    
    def _push(self, i):
        self._all_apply(i<<1, self.lazy[i])
        self._all_apply(i<<1|1, self.lazy[i])
        self.lazy[i] = self.id
    
    def update(self, k, x):
        """Updates the k-th element (0-indexed) to x. O(log n)"""
        k += self.size
        for i in range(self.log, 0, -1): self._push(k>>i)
        self.data[k] = x
        for i in range(1, self.log+1): self._update(k>>i)
    def __setitem__(self, k, x):
        k += self.size
        for i in range(self.log, 0, -1): self._push(k>>i)
        self.data[k] = x
        for i in range(1, self.log+1): self._update(k>>i)
            
    def apply(self, k, F):
        """Applies F to the k-th element (0-indexed). O(log n)"""
        k += self.size
        for i in range(self.log, 0, -1): self._push(k>>i)
        self.data[k] = mapping(F, self.data[k], self.len[k])
        for i in range(1, self.log+1): self._update(k>>i)
    
    def range_apply(self, l, r, F):
        """Applies F to the elements in [l, r) (0-indexed). O(log n)
        Here F is not a lambda function, but an encoded value which is
        passed to the mapping and composition functions."""
        if l == r: return
        l += self.size
        r += self.size
        for i in range(self.log, 0, -1):
            if ((l>>i)<<i) != l: self._push(l>>i)
            if ((r>>i)<<i) != r: self._push((r-1)>>i)
        l2, r2 = l, r
        while l < r:
            if l&1:
                self._all_apply(l, F)
                l += 1
            if r&1:
                r -= 1
                self._all_apply(r, F)
            l >>= 1
            r >>= 1
        l, r = l2, r2
        for i in range(1, self.log+1):
            if ((l>>i)<<i) != l: self._update(l>>i)
            if ((r>>i)<<i) != r: self._update((r-1)>>i)
        
    def range_update(self, l, r, x):
        """Assigns x to the elements in [l, r) (0-indexed). O(log n)"""
        self.range_apply(l, r, encode(0, x))

    def range_add(self, l, r, x):
        """Adds x to the elements in [l, r) (0-indexed). O(log n)"""
        self.range_apply(l, r, encode(1, x))

                
    def get(self, k):
        """Returns the k-th element (0-indexed). O(log n)"""
        k += self.size
        for i in range(self.log, 0, -1): self._push(k>>i)
        return self.data[k]
    def __getitem__(self, k):
        k += self.size
        for i in range(self.log, 0, -1): self._push(k>>i)
        return self.data[k]
    
    def query(self, l, r):
        """Returns op(a[l], ..., a[r-1]). O(log n)"""
        if l == r: return self.e
        l += self.size
        r += self.size
        for i in range(self.log, 0, -1):
            if ((l>>i)<<i) != l: self._push(l>>i)
            if ((r>>i)<<i) != r: self._push((r-1)>>i)   
        sml, smr = self.e, self.e
        while l < r:
            if l&1:
                sml = op(sml, self.data[l])
                l += 1
            if r&1:
                r -= 1
                smr = op(self.data[r], smr)
            l >>= 1
            r >>= 1
        return op(sml, smr)

    def max_right(self, l, func):
        """Returns r s.t. func(op(a[l], ..., a[r-1])) holds. O(log n)"""
        if l == self.n: return self.n
        l += self.size
        for i in range(self.log, 0, -1): self._push(l>>i)
        sm = self.e
        while 1:
            while not l&1: l >>= 1
            if not func(op(sm, self.data[l])):
                while l < self.size:
                    self._push(l)
                    l <<= 1
                    if func(op(sm, self.data[l])):
                        sm = op(sm, self.data[l])
                        l += 1
                return l - self.size
            sm = op(sm, self.data[l])
            l += 1
            if (l&-l) == l: break
        return self.n
    
    def max_left(self, r, func):
        """Returns l s.t. func(op(a[l], ..., a[r-1])) holds. O(log n)"""
        if r == 0: return 0
        r += self.size
        for i in range(self.log, 0, -1): self._push((r-1)>>i)
        sm = self.e
        while 1:
            r -= 1
            while r>1 and r&1: r >>= 1
            if not func(op(self.data[r], sm)):
                while r < self.size:
                    self._push(r)
                    r = r<<1|1
                    if func(op(self.data[r], sm)):
                        sm = op(self.data[r], sm)
                        r -= 1
                return r+1 - self.size
            sm = op(self.data[r], sm)
            if (r&-r) == r: break
        return 0
"""
Usage of LazySegmentTree(n, e, id_, A):
    N is the size of the array.
    e is the identity element of op.
    id_ is the identity element of mapping.
    A is the initial array.
    op is a binary operation. op(a, e) = op(e, a) = a.
    op must be associative. op(a, op(b, c)) = op(op(a, b), c).
"""
#def op(x, y):
#e =
#def composition(f, g):
#id_ =
#def mapping(f, x, size):
#seg = LazySegmentTree(N, e, id_, A)


# # Range Sum Query with Modulo
# mask = (1<<30)-1   # 1<<30 is used because it is just greater than 1e9
# def composition(f, g):
#     a, b = f>>30, f&mask
#     c, d = g>>30, g&mask
#     e, f = a*c, a*d+b
#     return (e%M)<<30|(f%M)
# id_ = 1<<30     # Identity element of mapping
# def mapping(f, x, size):
#     a, b = f>>30, f&mask
#     return (a*x + b*size)%M
# def op(x, y): return (x+y)%M
# e = 0           # Identity element of op


# Range Sum Query without Modulo
mask = (1<<30)-1  # 1<<30 is used because it is just greater than 1e9
def composition(f, g):
    a, b = f>>30, f&mask
    c, d = g>>30, g&mask
    e, f = a*c, a*d+b
    return e<<30|f
id_ = 1<<30     # Identity element of mapping
def mapping(f, x, size):
    a, b = f>>30, f&mask
    return a*x + b*size
def op(x, y): return x+y
e = 0           # Identity element of op


def encode(x, y): return x<<30|y
def decode(z): return z>>30, z&mask


A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
seg = LazySegmentTree(len(A), e, id_, A)
