
oo = 1 << 30

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    mn = [oo] * (n + 1)
    dp = [0] * (n + 1)
    for i in range(n):
        dp[i + 1] = min(dp[i] + 1, mn[arr[i]])
        mn[arr[i]] = min(mn[arr[i]], dp[i])
    print(n - dp[n])


