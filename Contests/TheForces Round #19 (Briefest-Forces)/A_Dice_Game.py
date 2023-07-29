import sys
input = sys.stdin.readline
print = lambda x: sys.stdout.write(str(x) + "\n")

def sigma(n):
    return n * (n + 1) >> 1

for _ in range(int(input())):
    l1, r1 = map(int, input().split())
    l2, r2 = map(int, input().split())
    e1 = (sigma(r1) - sigma(l1 - 1)) * (r2 - l2 + 1)
    e2 = (sigma(r2) - sigma(l2 - 1)) * (r1 - l1 + 1)
    print("YES" if e1 >= e2 else "NO")
