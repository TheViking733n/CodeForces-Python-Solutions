import sys
input = sys.stdin.readline


oo = 1 << 63
from collections import deque
class DisjointSetUnion:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_sets = n

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a

            self.num_sets -= 1
            self.parent[b] = a
            self.size[a] += self.size[b]

    def set_size(self, a):
        return self.size[self.find(a)]

    def __len__(self):
        return self.num_sets


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b):
        self.parent[self.find(b)] = self.find(a)




n, m = map(int, input().split())
W = [[oo] * n for _ in range(n)]
g = [[] for _ in range(n)]
dsu = DisjointSetUnion(n)
for _ in range(m):
    u, v, w = [int(x) - 1 for x in input().split()]; w += 1
    W[u][v] = W[v][u] = w
    g[u].append(v)
    g[v].append(u)
    dsu.union(u, v)

if dsu.find(0) != dsu.find(n - 1):
    print('inf')
    exit()

ans = []

q = deque([0])
vis = [0] * n
vis[0] = 1
while q:
    mn = (oo, oo, oo)
    for fst in q:
        for snd in g[fst]:
            if not vis[snd]:
                mn = min(mn, (W[fst][snd], fst, snd))
    if mn[0] == oo:
        break
    time, cur, other = mn
    # print(vis, time, cur, other)
    if vis[n-1] == 1: break

    
    if time != 0:
        ans.append((''.join(map(str, vis)), time))

    for fst in q:
        for snd in g[fst]:
            if not vis[snd]:
                W[fst][snd] -= time
                W[snd][fst] -= time

    cnt = 0
    for v in g[cur]:
        if not vis[v]:
            cnt += 1
    

    if cnt == 1: q.remove(cur)
    vis[other] = 1
    q.append(other)

ln = len(ans)
ln = min(ln, n * n)
tot = sum(x[1] for x in ans)
print(tot, ln)
for i in range(ln):
    print(*ans[i])
        













# if not g[n - 1]:
#     print('inf')
#     exit()

# out = [n - 1]
# for _ in range(5):
#     new_out = []
#     for u in out:
#         for v in g[u]:
#             if W[u][v] == 0:
#                 new_out.append(v)
#     out.extend(new_out)
#     print(out)
#     for out1 in out:
#         mn = oo
#         for v in g[out1]:
#             mn = min(mn, W[out1][v])
#     print(mn)
#     play(n, out, mn)

