# Don't use! Use SortedList instead. SortedList is 2x faster and indexable.

from heapq import heappush, heappop, heapify
from collections import defaultdict

class DeletableMinMaxPQ():
    def __init__(self, arr=[], isSet=False): # isSet: if True, then it is a set else it is a multiset
        self.minH = []
        self.maxH = []
        self.HC = defaultdict(int)
        self.size = 0
        self.isSet = isSet
        for x in arr:
            if self.isSet and self.HC[x] > 0:
                continue
            self.minH.append(x)
            self.maxH.append(-x)
            self.HC[x] += 1
            self.size += 1
        heapify(self.minH)
        heapify(self.maxH)

    def add(self, x: int) -> bool:
        if self.isSet and self.HC[x] > 0:
            return False
        heappush(self.minH, x)
        heappush(self.maxH, -x)
        self.HC[x] += 1
        self.size += 1
        return True

    def min(self) -> int:
        assert self.size > 0
        t = self.minH[0]
        while not self.HC[t]:
            heappop(self.minH)
            t = self.minH[0]
        return t

    def extractMin(self) -> int:
        assert self.size > 0
        t = heappop(self.minH)
        while not self.HC[t]:
            t = heappop(self.minH)
        self.HC[t] -= 1
        self.size -= 1
        return t
    
    def max(self) -> int:
        assert self.size > 0
        t = self.maxH[0]
        while not self.HC[-t]:
            heappop(self.maxH)
            t = self.maxH[0]
        return -t
    
    def extractMax(self) -> int:
        assert self.size > 0
        t = -heappop(self.maxH)
        while not self.HC[t]:
            t = -heappop(self.maxH)
        self.HC[t] -= 1
        self.size -= 1
        return t
    
    def remove(self, x) -> bool:
        if self.HC[x] > 0:
            self.HC[x] -= 1
            self.size -= 1
            return True
        return False
    
    def __contains__(self, x: int) -> bool:
        return self.HC[x] > 0
    
    def __len__(self):
        return self.size
    
    def __bool__(self):
        return self.size > 0
    
    def __repr__(self):
        items = []
        for k in self.HC:
            items.extend([k]*self.HC[k])
        return str(sorted(items))