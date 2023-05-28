import os,sys
from io import BytesIO, IOBase

"""
We are given N, and we have to check if it is possible to
write it as a sum of consecutive positive integers.

If it is possible, we have to print the possible length of the sequence.

Let the sequence be [a, a+1, a+2, ..., a+k-1]
Then, (a + a+k-1) * k / 2 = N
=> (2a + k - 1) * k = 2N
Let decompose N into even and odd factors.
N = 2^(p-1) * m, where m is odd.

    => (2a + k - 1) * k = 2^p * m       ---(1)

If k is odd, then 2a + k - 1 is even.
    => (2a + k - 1) = 2^p and k = m     ---(2)
    => a = (2^p - m + 1) / 2
    Since a is positive
    => 2^p - m >= 0

If k is even, then 2a + k - 1 is odd.
    => (2a + k - 1) = m and k = 2^p     ---(3)
    => a = (m - 2^p + 1) / 2
    Since a is positive
    => m - 2^p >= 0

From (2) and (3), we can see that
    k = min(m, 2^p)
"""

def isPowerOfTwo(n):
    return n & (n - 1) == 0

def main():
    for _ in range(int(input())):
        n = int(input())
        if isPowerOfTwo(n):
            print(-1)
            continue

        p = 1
        while n & 1 == 0:
            p += 1
            n >>= 1
        print(min(1 << p, n))

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# =============================== Region Fastio ===============================
if not os.path.isdir('C:/users/acer'):
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

# =============================== Endregion ===============================

if __name__ == "__main__":
    #read()
    main()
    #dmain()
