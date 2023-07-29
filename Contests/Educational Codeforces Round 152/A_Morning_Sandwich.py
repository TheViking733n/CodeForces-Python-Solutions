import sys
input = sys.stdin.readline
oo = 1 << 60

def solve():
    b, c, h = map(int, input().split())
    spread = c + h
    b -= 1
    ans = 1 + min(b, spread) * 2
    print(ans)

for _ in range(int(input())):
    solve()

