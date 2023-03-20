from __future__ import division, print_function
import os,sys
from io import BytesIO, IOBase
from random import randint, randrange
if sys.version_info[0] < 3:
    from __builtin__ import range as range
    from future_builtins import ascii, filter, hex, map, oct, zip


from math import ceil, floor, factorial, log10
# from math import log,sqrt,cos,tan,sin,radians
from bisect import bisect_left, bisect_right
from collections import deque, Counter, defaultdict
# from bisect import bisect,bisect_left,bisect_right,insort,insort_left,insort_right
# from decimal import *
# from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace
# from collections import OrderedDict
# from itertools import permutations


M=1000000007
# M=998244353
INF = float("inf")
PI = 3.141592653589793
R = randrange(2, 1 << 32)
# R = 0          # Enable this for debugging of dict keys in myDict

# ========================= Main ==========================


class pal_node:
    def __init__(self):
        # start and end indices of the palindrome
        self.start = None
        self.end = None
    
        # length of the palindrome
        self.length = None
    
        # edges to the palindromes that are formed by padding the same 
        # letter on the front and back of this palindrome
        self.pad = [None for _ in range(26)]
                        
        # edge to this palindrome's longest palindromic suffix                        
        self.suffix = None
        
        # number of occurrences of this palindrome
        self.num_occ = 1
        
        self.characteristic = 1
    

class pal_tree: 
    def __init__(self, s):
        self.s = s
        self.root1 = pal_node()
        self.root2 = pal_node()
        self.root1.length = -1
        self.root2.length = 0
        self.root1.suffix = self.root1
        self.root2.suffix = self.root1
        self.curr_node = self.root1
        self.palindromes = [] # stores the nodes in the order they're created
        self.num_dist_pal = 0    
     
    def insert(self, i):    
        temp = self.curr_node
        
        # look for X such that s[i]Xs[i] is a palindrome
        while True:
            curr_length = temp.length
            if i - curr_length >= 1 and self.s[i] == self.s[i-curr_length-1]:
                break
            temp = temp.suffix        
    
        # check if s[i]Xs[i] already exists
        if temp.pad[ord(self.s[i])-ord('a')]:
            self.curr_node = temp.pad[ord(self.s[i])-ord('a')]
            self.curr_node.num_occ += 1
            return
    
        new_node = pal_node()
        temp.pad[ord(self.s[i])-ord('a')] = new_node
        new_node.length = temp.length + 2
        new_node.start = i - new_node.length + 1
        new_node.end = i
        new_pal = self.s[new_node.start:new_node.end+1]
        self.num_dist_pal += 1
        self.palindromes.append(new_node)
    
        if new_node.length == 1:
            new_node.suffix = self.root2
            self.curr_node = new_node
            return
    
        temp = temp.suffix
        while True:
            curr_length = temp.length
            if i - curr_length >= 1 and self.s[i] == self.s[i-curr_length-1]:
                break
            temp = temp.suffix
    
        new_node.suffix = temp.pad[ord(self.s[i])-ord('a')]
        
        # get the characteristic of the new node
        temp = new_node
        while temp.length > new_node.length//2:
            temp = temp.suffix
        if temp.length == new_node.length//2:
            new_node.characteristic = temp.characteristic + 1
            
        self.curr_node = new_node    
        
    def compute_occurrences(self):
        for i in range(-1, -self.num_dist_pal-1, -1):
            self.palindromes[i].suffix.num_occ += self.palindromes[i].num_occ
                
        
                                
def main():
    TestCases = 1
    
    for _ in range(TestCases):
        # n,k = [int(i) for i in input().split()]
        s = input()
        n = len(s)

        # # DP Solution

        dp = [[0 for _ in range(n)] for _ in range(n)]

        ans = [0] * n

        for i in range(n):
            dp[i][i] = 1
        
        ans[0] += n
        
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 2
                ans[1] += 1
            else:
                dp[i][i+1] = 0
        

        for ln in range(3, n + 1):
            i, j = 0, ln - 1
            while j < n:
                if s[i] != s[j] or dp[i+1][j-1] == 0:
                    dp[i][j] = 0
                elif s[i] == s[j]:
                    dp[i][j] = dp[i][(i + j + 1) // 2 - 1] + 1
                    ans[dp[i][j]-1] += 1
                i += 1
                j += 1
        
        # print(*dp, sep='\n')
        
        sm = 0
        for i in range(n-1, -1, -1):
            sm += ans[i]
            ans[i] = sm


        print(*ans)
        










        # # Palindromic Tree solution


        # tree = pal_tree(s)
            
        # for i in range(len(s)):
        #     tree.insert(i)  
            
        # tree.compute_occurrences()

        # ch = [0]*len(s)
        # for pal in tree.palindromes:
        #     for c in range(1, pal.characteristic+1):
        #         ch[c-1] += pal.num_occ
        # print(*ch)     



















        # # My solution that doesn't work :'/

        # arr = [1<<(ord(i) - ord('a')) for i in s]

        # seg1 = SegmentTree(arr, default=0, func=lambda a, b: a + b)
        # seg2 = SegmentTree(arr, default=0, func=lambda a, b: a ^ b)
        # seg3 = SegmentTree(arr, default=1, func=lambda a, b: (a * b) % M)
        # ps = [0] + list(accumulate(arr))

        # ans1 = 0
        # palin = defaultdict(list)
        # for i in range(n):
        #     j1, j2 = i, i
        #     while j1 >= 0 and j2 < n and s[j1] == s[j2]:
        #         ans1 += 1
        #         palin[j2 - j1 + 1].append((j1, j2))
        #         j1 -= 1
        #         j2 += 1

        
        # for i in range(n-1):
        #     j1, j2 = i, i+1
        #     while j1 >= 0 and j2 < n and s[j1] == s[j2]:
        #         ans1 += 1
        #         palin[j2 - j1 + 1].append((j1, j2))
        #         j1 -= 1
        #         j2 += 1
        

        # ans = [ans1]
        # while palin:
        #     palin2 = defaultdict(list)
        #     ans2 = 0

        #     for ln in palin:
        #         # palin[ln].sort()
        #         for j1, j2 in palin[ln]:
        #             x1, y1 = j2 + 1, j2 + 2
        #             x2, y2 = x1 + ln - 1, y1 + ln - 1

        #             for st, en in [(x1, x2), (y1, y2)]:
        #                 idx = bisect_left(palin[ln], (st, en))
        #                 if idx < len(palin[ln]) and palin[ln][idx] == (st, en):
        #                     # eq1 = seg1.query(j1, j2+1) == seg1.query(st, en+1)
        #                     # eq2 = seg2.query(j1, j2+1) == seg2.query(st, en+1)
        #                     # if not eq1:
        #                         # continue
        #                     # eq3 = seg3.query(j1, j2+1) == seg3.query(st, en+1)
        #                     # equal = eq1 and eq3

        #                     if ps[j2+1] - ps[j1] != ps[en+1] - ps[st]:
        #                         continue

        #                     equal = True
        #                     for k in range(ln//2+1):
        #                         if s[j1 + k] != s[st + k]:
        #                             equal = False
        #                             break
        #                     if equal:
        #                         palin2[en - j1 + 1].append((j1, en))
        #                         ans2 += 1
        #     ans.append(ans2)
        #     palin = palin2
        
        
        # ans.extend([0]*(n-len(ans)))
        # print(*ans)
                            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# ======================== Functions declaration Starts ========================
abc='abcdefghijklmnopqrstuvwxyz'
abd={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}

def copy2d(lst): return [x[:] for x in lst]   #Copy 2D list... Avoid Using Deepcopy
def no_of_digits(num): return 0 if num <= 0 else int(log10(num)) + 1
def powm(num, power, mod=M): return pow(num, power, mod)
def isPowerOfTwo(x): return (x and (not(x & (x - 1))))
def LSB(num):
    """Returns Least Significant Bit of a number (Rightmost bit) in O(1)"""
    return num & -num

def MSB(num):
    """Returns Most Significant Bit of a number (Leftmost bit) in O(logN)"""
    if num <= 0: return 0
    ans = 1; num >>= 1
    while num:
        num >>= 1; ans <<= 1
    return ans


LB = bisect_left   # Lower bound
UB = bisect_right  # Upper bound
 
def BS(a, x):      # Binary Search
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    else:
        return -1

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return (x*y)//gcd(x,y)


# import threading
# def dmain():
#     sys.setrecursionlimit(1000000)
#     threading.stack_size(1024000)
#     thread = threading.Thread(target=main)
#     thread.start()
            
# =============================== Custom Classes ===============================

class Wrapper(int):
    def __init__(self, x):
        int.__init__(x)
    def __hash__(self):
        return super(Wrapper, self).__hash__() ^ R
Int = lambda x:Wrapper(int(x))        

class myDict():
    def __init__(self,func=int):
        # self.RANDOM = randint(0,1<<32)
        self.RANDOM = R
        self.default=func
        self.dict={}
    def __getitem__(self,key):
        myKey=self.RANDOM^key
        if myKey not in self.dict:
            self.dict[myKey]=self.default()
        return self.dict[myKey]
    def __setitem__(self,key,item):
        myKey=self.RANDOM^key
        self.dict[myKey]=item
    def __contains__(self,key):
        myKey=self.RANDOM^key
        return myKey in self.dict
    def __delitem__(self,key):
        myKey=self.RANDOM^key
        del self.dict[myKey]
    def keys(self):
        return [self.RANDOM^i for i in self.dict]


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
