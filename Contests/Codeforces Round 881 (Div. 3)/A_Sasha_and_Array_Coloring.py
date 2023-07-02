import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=1)
    sz = len(a) >> 1
    print(max(0, sum(a[:sz]) - sum(a[-sz:])))