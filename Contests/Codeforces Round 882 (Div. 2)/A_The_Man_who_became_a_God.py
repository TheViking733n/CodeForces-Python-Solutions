import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = 0
    a2 = [0]
    for i in range(1, n):
        x = abs(arr[i] - arr[i-1])
        a2.append(x)
    a2.sort()
    # print(a2)
    print(sum(a2[:n-k+1]))
