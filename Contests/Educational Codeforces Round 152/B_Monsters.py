import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    a3 = [((arr[i] - 1) % k + 1, ~i) for i in range(n)]
    print(*[-i[1] for i in sorted(a3, reverse=1)])