from __future__ import division, print_function

import sys, os, __pypy__
from collections import defaultdict
from cStringIO import StringIO
from io import IOBase
range = xrange
input = raw_input

def main():

    inp = [int(x) for x in sys.stdin.read().split()]; ii = 0
    
    t = inp[ii]; ii += 1
    for _ in range(t):
        n = inp[ii]; ii += 1
        arr = inp[ii: ii + n]; ii+=n
        ans = 0
        for i in range (1,n):
            bigger = max(arr[i],arr[i-1])
            smaller = min(arr[i],arr[i-1])
            while(bigger>2*smaller):
                smaller*=2
                ans += 1
        print(ans)


# region fasto
 
BUFSIZE = 8192

 
class FastO(IOBase):
    def __init__(self, file):
        self._fd = file.fileno()
        self._buffer = __pypy__.builders.StringBuilder()
        self.write = lambda s: self._buffer.append(s)
 
    def flush(self):
        os.write(self._fd, self._buffer.build())
        self._buffer = __pypy__.builders.StringBuilder()
 
sys.stdout = FastO(sys.stdout)

 
# endregion
 
if __name__ == "__main__":
    main()