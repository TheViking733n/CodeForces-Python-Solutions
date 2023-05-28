# https://cses.fi/problemset/hack/1735/entry/176208/
# Pajenegod implementation, similar to pyrival template and faster for no modulo operations

class LazySegmentTree:
    def __init__(self, data, padding = 0):
        """initialize the lazy segment tree with data"""
        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()
        
        self.data = [padding] * (2 * _size)
        self.data[_size:_size + self._len] = data
        for i in reversed(range(1, _size)):
            self.data[i] = self.data[2 * i] + self.data[2 * i + 1]     
        self._lazy = [1,0] * (2 * _size)
 
    def _push(self, idx):
        """push query on idx to its children"""
        # Let the children know of the queries
        idx *= 2
        a = self._lazy[idx]
        b = self._lazy[idx + 1] >> 1
        self._lazy[idx] = 1
        self._lazy[idx + 1] = 0
        
        self.data[idx] = a * self.data[idx] + b
        self.data[idx + 1] = a * self.data[ idx + 1] + b
        
        idx *= 2
        self._lazy[idx] = a * self._lazy[idx] 
        self._lazy[idx + 1] = a * self._lazy[idx + 1] + b
        self._lazy[idx + 2] = a * self._lazy[idx + 2]
        self._lazy[idx + 3] = a * self._lazy[idx + 3] + b
    
    def _build(self, idx):
        """make the changes to idx be known to its ancestors"""
        idx >>= 1
        while idx:
            # TODO
            self.data[idx] = self.data[2 * idx] + self.data[2 * idx + 1]
            idx >>= 1
 
    def _update(self, idx):
        """updates the node idx to know of all queries applied to it via its ancestors"""
        for i in reversed(range(1, idx.bit_length())):
            self._push(idx >> i)
 
    def add(self, start, stop, ab):
        """lazily add value to [start, stop)"""
        a, b = ab
        start = start_copy = start + self._size
        stop = stop_copy = stop + self._size
 
        # Apply all the lazily stored queries
        self._update(start); self._update(stop - 1)
 
        while start < stop:
            if start & 1:
                self.data[start] = a * self.data[start] + b
                self._lazy[2 * start] = a * self._lazy[2 * start]
                self._lazy[2 * start + 1] = a * self._lazy[2 * start + 1] + b
                start += 1
            if stop & 1:
                stop -= 1
                self.data[stop] = a * self.data[stop] + b
                self._lazy[2 * stop] = a * self._lazy[2 * stop]
                self._lazy[2 * stop + 1] = a * self._lazy[2 * stop + 1] + b
            start >>= 1; stop >>= 1; b <<= 1
        
        while not start_copy&1: start_copy >>= 1
        while not stop_copy&1: stop_copy >>= 1
        self._build(start_copy); self._build(stop_copy - 1)
 
    def query(self, start, stop, res = 0):
        """func of data[start, stop)"""
        start += self._size; stop += self._size
 
        # Apply all the lazily stored queries
        self._update(start); self._update(stop - 1)
        while start < stop:
            if start & 1:
                res += self.data[start]
                start += 1
            if stop & 1:
                stop -= 1
                res += self.data[stop]
            start >>= 1; stop >>= 1
        return res
 
def main():
    n, q = [int(i) for i in input().split()]
    arr = [int(i) for i in input().split()]
    seg = LazySegmentTree(arr)

    for _ in range(q):
        t, a, b, *x = map(int, input().split())
        if x: x = x[0]
        if t == 1:
            seg.add(a-1, b, (1, x))    # arr[i] += x  (Add)
        elif t == 2:
            seg.add(a-1, b, (0, x))    # arr[i] = x  (Update)
        else:
            print(seg.query(a-1, b))