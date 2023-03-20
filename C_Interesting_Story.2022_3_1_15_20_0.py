from __future__ import division, print_function
import os
import sys
from io import BytesIO, IOBase


from bisect import bisect_left, bisect_right
from math import gcd, lcm    # Use gcd(*arr) to pass a list
from math import ceil, floor


# ======================== Functions declaration Starts ========================

LB = bisect_left
UB = bisect_right
 
def BS(a, x):    # Binary Search
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    else:
        return -1



# ========================= Functions declaration Ends =========================


def main():
    TestCases = 1
    TestCases = int(input())

    for _ in range(TestCases):
        # n,x,y = [int(i) for i in input().split()]
        n = int(input())
        # arr = [int(i) for i in input().split()]
        # s = input()
        arr = [input() for i in range(n)]

        total = [[0,0],[0,1],[0,2],[0,3],[0,4]]
        cnt_arr = []
        for word in arr:
            temp = [0]*5
            for letter in word:
                x=ord(letter)-97
                total[x][0]+=1
                temp[x]+=1
            cnt_arr.append(temp)

        
        total.sort(reverse=True)
        # print(total)

        
        rep_mx = total[0][1]
        
        iska_tot = total[0][0]
        baaki_tot = sum([total[i][0] for i in range(1,5)])

        diff = [] # [baaki-iska, index]

        for i in range(n):
            cnt = cnt_arr[i]
            iska = cnt[rep_mx]
            baaki = sum(cnt)-iska

            diff.append([baaki-iska, i])
        
        diff.sort(reverse=True)
        # print(rep_mx,iska_tot,diff)
        ans = n

        for p in diff:
            ind = p[1]
            cnt = cnt_arr[ind]
            iska = cnt[rep_mx]
            baaki = sum(cnt)-iska

            if iska_tot > baaki_tot:
                break

            else:
                iska_tot -= iska
                baaki_tot -= baaki
                ans -= 1
        
        print(ans)




















# =============================== Template Starts ===============================

if sys.version_info[0] < 3:
    class dict(dict):
        def items(self):
            return dict.iteritems(self)
 
        def keys(self):
            return dict.iterkeys(self)
 
        def values(self):
            return dict.itervalues(self)
    from __builtin__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip

# region fastio

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._file = file
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


def print(*args, **kwargs):
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop("sep", " "), kwargs.pop("file", sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        file.write(str(x))
        at_start = False
    file.write(kwargs.pop("end", "\n"))
    if kwargs.pop("flush", False):
        file.flush()


if sys.version_info[0] < 3:
    sys.stdin, sys.stdout = FastIO(sys.stdin), FastIO(sys.stdout)
else:
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)

input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion

if __name__ == "__main__":
    main()