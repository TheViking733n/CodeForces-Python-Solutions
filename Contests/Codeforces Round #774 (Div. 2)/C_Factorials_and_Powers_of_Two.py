import sys,os,io

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
# input = sys.stdin.readline




facts = [6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800, 479001600, 6227020800, 87178291200, 1307674368000]

g = {}

def fun(facts, i, cnt, mx, s):
    if i == len(facts):
        return
    
    if cnt == mx and s<=1e12:
        if bin(s).count('1') > mx:
            g[s] = mx
            return

    fun(facts, i+1, cnt+1, mx, s+facts[i])
    fun(facts, i+1, cnt, mx, s)

for i in range(len(facts), 0, -1):
    fun(facts, 0, 0, i, 0)





TestCases = 1
TestCases = int(input())

for _ in range(TestCases):
    # n,x,y = [int(i) for i in input().split()]
    n = int(input())
    # arr = [int(i) for i in input().split()]
    # s = input()



    b = bin(n)[2:]
    ones = b.count('1')
    # zeros = len(b) - ones

    ans = ones

    for k in g:
        if k <= n:
            v = g[k]
            m = n-k
            ones = bin(m)[2:].count('1')
            a = v + ones

            if a < ans:
                ans = a
    
    print(ans)

