import os
import sys
from io import BytesIO, IOBase

_str = str
str = lambda x=b"": x if type(x) is bytes else _str(x).encode()

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


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")


from heapq import heappop, heappush
oo = 1 << 63

def inp(): return int(input(), 2)
def encode(x, y): return (x << 10) | y
def decode(z): return z >> 10, z & 1023

def dijkstra(graph, start):
    n = len(graph)
    dist = [oo] * n
    dist[start] = 0

    queue = [encode(0, start)]
    while queue:
        path_len, v = decode(heappop(queue))
        if path_len == dist[v]:
            for w, edge_len in graph[v]:
                if edge_len + path_len < dist[w]:
                    dist[w] = edge_len + path_len
                    heappush(queue, encode(edge_len + path_len, w))
    return dist[0]


for _ in range(int(input())):
    n, m = map(int, input().split())
    init = inp()
    N = 1 << n
    mask = N - 1
    medi = [(int(input()), mask ^ inp(), inp()) for _ in range(m)]
    mat = [[oo] * N for _ in range(N)]
    for u in range(N):
        for d, c, e in medi:
            v = (u & c) | e
            mat[u][v] = min(mat[u][v], d)
    
    g = [[] for _ in range(N)]
    for u in range(N):
        for v in range(N):
            if mat[u][v] != oo:
                g[u].append((v, mat[u][v]))
    
    dist = dijkstra(g, init)
    print(dist if dist != oo else -1)
    



    