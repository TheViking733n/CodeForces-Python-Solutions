import sys
import random
from collections import defaultdict
from itertools import permutations

input = sys.stdin.readline
print = lambda x: sys.stdout.write(str(x) + "\n")
class DefaultDict:
    def __init__(self, default=None):
        self.default = default
        self.x = random.randrange(1, 1 << 31)
        self.dd = defaultdict(default)
 
    def __repr__(self):
        return "{"+", ".join(f"{k ^ self.x}: {v}" for k, v in self.dd.items())+"}"
 
    def __eq__(self, other):
        for k in set(self) | set(other):
            if self[k] != other[k]: return False
        return True
 
    def __or__(self, other):
        res = DefaultDict(self.default)
        for k, v in self.dd: res[k] = v
        for k, v in other.dd: res[k] = v
        return res
 
    def __len__(self):
        return len(self.dd)
 
    def __getitem__(self, item):
        return self.dd[item ^ self.x]
 
    def __setitem__(self, key, value):
        self.dd[key ^ self.x] = value
 
    def __delitem__(self, key):
        del self.dd[key ^ self.x]
 
    def __contains__(self, item):
        return item ^ self.x in self.dd
 
    def items(self):
        for k, v in self.dd.items(): yield (k ^ self.x, v)
 
    def keys(self):
        for k in self.dd: yield k ^ self.x
 
    def values(self):
        for v in self.dd.values(): yield v
 
    def __iter__(self):
        for k in self.dd: yield k ^ self.x
 
class Counter(DefaultDict):
    def __init__(self, aa=[]):
        super().__init__(int)
        for a in aa: self.dd[a ^ self.x] += 1
 
    def __add__(self, other):
        res = Counter()
        for k in set(self) | set(other):
            v = self[k]+other[k]
            if v > 0: res[k] = v
        return res
 
    def __sub__(self, other):
        res = Counter()
        for k in set(self) | set(other):
            v = self[k]-other[k]
            if v > 0: res[k] = v
        return res
 
    def __and__(self, other):
        res = Counter()
        for k in self:
            v = min(self[k], other[k])
            if v > 0: res[k] = v
        return res
 
    def __or__(self, other):
        res = Counter()
        for k in set(self) | set(other):
            v = max(self[k], other[k])
            if v > 0: res[k] = v
        return res

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

acnt = Counter(a)
bcnt = Counter(b)
ccnt = Counter(c)

ans = 0
for i in range(1, m + 1):
    other = m // i
    if other < i: break
    if m % i: continue
    for j in range(1, other + 1):
        k = other // j
        if k < j: break
        if other % j: continue
        if [i, j, k] != sorted((i, j, k)): continue
        seen = set()
        for p in permutations((i, j, k)):
            if p in seen: continue
            seen.add(p)
            ans += acnt[p[0]] * bcnt[p[1]] * ccnt[p[2]]
print(ans)