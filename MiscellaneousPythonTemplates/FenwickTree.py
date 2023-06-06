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