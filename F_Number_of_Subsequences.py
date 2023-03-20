from __future__ import division, print_function
import os,sys
from io import BytesIO, IOBase
if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip



M=1000000007

# ========================= Main ==========================



def main():
    def conv(ele):
        v = [0] * 4
        v[ele] += 1
        return v

    def add(v1, ele):
        sm = [0] * 4
        v2 = conv(ele)
        for i in range(4):
            sm[i] += v1[i] + v2[i]
        return sm
    
    pow3 = [1]
    for i in range(1, 200005):
        pow3.append((pow3[-1] * 3) % M)

    def cnt(a, q):
        if q == 0:
            return a
        return (q + 3 * a) * pow3[q - 1]
        
    
    # n,k = [int(i) for i in input().split()]
    n = int(input())
    # arr = [int(i) for i in input().split()]
    s = input()
    hsh = {'?':0,'a':1,'b':2,'c':3}
    arr = [hsh[i] for i in s]

    pre = [conv(arr[0])]
    suf = [conv(arr[-1])]
    for i in range(1, n):
        pre.append(add(pre[-1], arr[i]))
        suf.append(add(suf[-1], arr[n - i - 1]))
    suf.reverse()

    # print(pre)
    # print(suf)
    ans = 0
    for i in range(1, n-1):
        if arr[i] not in [0, 2]:
            continue
        x, y = pre[i-1], suf[i+1]
        q1, a = x[0], x[1]
        q2, c = y[0], y[3]
        ans += cnt(a, q1) * cnt(c, q2)
        ans %= M
    print(ans)




        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# ======================== Functions declaration Starts ========================
# import threading
# def dmain():
#     sys.setrecursionlimit(1000000)
#     threading.stack_size(1024000)
#     thread = threading.Thread(target=main)
#     thread.start()
            
# =============================== Custom Classes ===============================


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
