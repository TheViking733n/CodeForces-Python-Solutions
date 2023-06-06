class FenwickTree:
    def __init__(self, x):
        """transform list into BIT"""
        self.arr = x
        x = self.bit = x[:]
        for i in range(len(x)):
            j = i | (i + 1)
            if j < len(x):
                x[j] += x[i]

    def update(self, idx, x):
        """updates bit[idx] += x"""
        self.arr[idx] += x
        while idx < len(self.bit):
            self.bit[idx] += x
            idx |= idx + 1

    def __getitem__(self, idx):
        return self.arr[idx]
    
    def __setitem__(self, idx, x):
        """updates bit[idx] = x"""
        self.update(idx, x - self.arr[idx])
    
    def __iadd__(self, idx, x):
        """updates bit[idx] += x"""
        self.update(idx, x)


    def _sum(self, end):
        """calc sum from [0, end) (zero based)"""
        x = 0
        try:
            while end > 0:
                x += self.bit[end - 1]
                end &= end - 1
            return x
        except:
            print(end)
            exit(1)
    
    def query(self, begin, end):
        """calc sum from [begin, end) (zero based)"""
        if begin >= end:
            return 0
        return self._sum(end) - self._sum(begin)

    def findkth(self, k):
        """Find largest idx such that sum from [0, idx) <= k"""
        idx = -1
        for d in reversed(range(len(self.bit).bit_length())):
            right_idx = idx + (1 << d)
            if right_idx < len(self.bit) and k >= self.bit[right_idx]:
                idx = right_idx
                k -= self.bit[idx]
        return idx + 1
    
    def __repr__(self):
        return "BIT({})".format(self.arr)


class SortedMultiSet:
    def __init__(self, iterable=[], max_n=2 * 10**5):
        """Initialize sorted list instance."""
        self.N = max_n + 1
        self.fen = FenwickTree([0] * self.N)
        self.size = len(iterable)
        for x in iterable:
            self.fen.update(x, 1)
    
    def __getitem__(self, idx):
        """Lookup value at `idx`."""
        if not -self.size <= idx < self.size:
            raise IndexError("list index out of range")
        if idx < 0:
            idx += self.size
        return self.fen.findkth(idx + 1)
    
    def remove(self, x):
        """Remove first occurrence of value."""
        assert 0 <= x < self.N
        if self.fen[x] == 0:
            return False
        self.fen.update(x, -1)
        self.size -= 1
        return True

    def add(self, x):
        """Add value to sorted list."""
        assert 0 <= x < self.N
        self.fen.update(x, 1)
        self.size += 1

    def __contains__(self, x):
        """Return true if `x` in sorted list."""
        assert 0 <= x < self.N
        return self.fen[x] > 0
    
    def max(self):
        """Return max value in sorted list."""
        assert self.size > 0
        return self.fen.findkth(self.size-1)
    
    def min(self):
        """Return min value in sorted list."""
        assert self.size > 0
        return self.fen.findkth(0)
    
    def __len__(self):
        """Return the size of sorted list."""
        return self.size
    
    def __bool__(self):
        """Return `True` when sorted list is not empty."""
        return not self.size == 0

    def __repr__(self):
        """Return string representation of sorted list."""
        ans = []
        for i in range(self.N):
            ans.extend([i] * self.fen[i])
        return "SortedMultiSet({})".format(ans)


