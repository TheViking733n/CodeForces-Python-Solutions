import sys
input = sys.stdin.readline
from itertools import accumulate
oo = 1 << 30
for _ in range(int(input())):
    n, m = map(int, input().split())
    segs = [tuple(int(i) - 1 for i in input().split()) for _ in range(m)]
    q = int(input())
    ind = [int(input()) - 1 for _ in range(q)]
    low, high = 0, q-1
    ans = oo
    while low <= high:
        mid = low + high >> 1
        arr = [0] * n
        for i in range(mid+1): arr[ind[i]] = 1
        ps = [0] + list(accumulate(arr))
        done = False
        for l, r in segs:
            one = ps[r+1] - ps[l]
            zero = r - l + 1 - one
            if one > zero:
                done = True
                break
        if done:
            ans = min(ans, mid+1)
            high = mid - 1
        else:
            low = mid + 1
    if ans == oo: ans = -1
    print(ans)
