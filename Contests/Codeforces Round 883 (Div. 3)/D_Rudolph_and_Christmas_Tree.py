import sys
input = sys.stdin.readline
print = lambda x: sys.stdout.write(str(x) + "\n")


for _ in range(int(input())):
    n, b, h = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = b * h * n / 2
    for i in range(1, n):
        diff = arr[i] - arr[i - 1]
        if diff >= h: continue
        ans -= ((h - diff) * (h - diff) * b) / (2 * h)
    print(ans)

    