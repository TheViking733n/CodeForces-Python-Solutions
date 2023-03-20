import os
import sys
from io import BytesIO, IOBase
from bisect import bisect_left, bisect_right

LB = bisect_left
UB = bisect_right
 
def BS(a, x):    # Binary Search
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    else:
        return -1


def main():
    TestCases = 1
    TestCases = int(input())

    for _ in range(TestCases):
        # n,x,y = [int(i) for i in input().split()]
        n = int(input())
        # arr = [int(i) for i in input().split()]
        # s = input()
        arr = [input() for i in range(n)]

        total = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0}
        cnt_arr = []
        s=0
        for word in arr:
            temp = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0}
            for letter in word:
                temp[letter] += 1
                total[letter] += 1
            temp["sum"]=len(word)
            s += temp["sum"]
            cnt_arr.append(temp)
        total["sum"] = s

        answers = []
        for ch in "abcde":
            iska_tot = total[ch]
            baaki_tot = total["sum"]-iska_tot
            
            iska = cnt_arr[0][ch]
            baaki = cnt_arr[0]["sum"]-iska
            diff = [baaki-iska]
            for i in range(1, n):
                iska = cnt_arr[i][ch]
                baaki = cnt_arr[i]["sum"]-iska
                diff.append(baaki-iska+diff[-1])
                
            
            ans = n
            diff.sort()
            
            d = baaki_tot-iska_tot

            if d>=0:
                x = LB(diff, d)
                ans = x-1+100
            else:
                ans = n+100

            answers.append(ans)

        print(max(answers))





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


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion

if __name__ == "__main__":
    main()
