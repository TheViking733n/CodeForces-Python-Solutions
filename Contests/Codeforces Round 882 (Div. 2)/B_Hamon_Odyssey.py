import sys
input = sys.stdin.readline
print = lambda x: sys.stdout.write(str(x) + '\n')
from collections import deque
oo = (1 << 31) - 1

for _ in range(int(input())):
    n = int(input())
    arr = deque(map(int, input().split()))
    a = arr[0]
    for i in range(1, n):
        a &= arr[i]
    cnt = 0
    cur = oo
    while arr:
        cur &= arr.popleft()
        if cur == 0:
            cnt += 1
            cur = oo
    cur = oo
    while arr:
        cur &= arr.pop()
        if cur == 0:
            cnt += 1
            cur = oo
    if cnt == 0: cnt += 1
    print(cnt)