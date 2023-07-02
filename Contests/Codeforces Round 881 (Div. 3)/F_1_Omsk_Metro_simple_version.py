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




from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

@bootstrap
def dfs(u, pa, g, W, queries, ans, ps, mn, mx, mnsum, mxsum):
    ps += W[u]
    mn = min(mn, ps); mx = max(mx, ps)
    mxsum = max(mxsum, ps - mn); mnsum = min(mnsum, ps - mx)
    for tar, qi in queries[u]:
        ans[qi] = (mnsum <= tar and tar <= mxsum)
    for v in g[u]:
        if v != pa:
            yield dfs(v, u, g, W, queries, ans, ps, mn, mx, mnsum, mxsum)
    yield

for _ in range(int(input())):
    n = int(input())
    queries = [[] for _ in range(n+1)]; sz, qi = 1, 0
    g = [[] for _ in range(n+1)]
    W = [0] * (n + 1); W[0] = 1
    for _ in range(n):
        ch, *args = input().split()
        if ch == '+':
            u, w = map(int, args); u -= 1
            g[u].append(sz)
            g[sz].append(u)
            W[sz] = w
            sz += 1
        else:
            st, en, tar = map(int, args); st -= 1; en -= 1
            queries[en].append((tar, qi))
            qi += 1
    ans = [0] * qi
    dfs(0, -1, g, W, queries, ans, 0, 0, 0, 0, 0)
    print(*["YES" if x else "NO" for x in ans], sep='\n')


