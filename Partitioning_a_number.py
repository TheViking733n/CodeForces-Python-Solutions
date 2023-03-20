# Recursive

def partition(n, k):    # No. of partition of n using 1, 2, 3, 4, ..., k
    if n < 0: return 0
    if n == 0: return 1
    if k < 1: return 0
    return partition(n, k - 1) + partition(n - k, k)




# Using dynamic programming

def partition_dp(n, k):  # No. of partition of n using 1, 2, 3, 4, ..., k
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(k + 1):
        dp[0][i] = 1
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            dp[i][j] = dp[i][j - 1] + (dp[i - j][j] if i >= j else 0)
    return dp[n][k]


# Apply space optimisation

def partition_dp(n, k):  # No. of partition of n using 1, 2, 3, 4, ..., k
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, k + 1):
        for j in range(i, n + 1):
            dp[j] += dp[j - i]
    return dp[n]



# Using dynamic programming and generalised for any array

def partition_generalised(n, arr): # No. of partition of n using only arr
    # Note: arr must be sorted
    arr = sorted(arr)
    k = len(arr)
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in arr:
        for j in range(i, n + 1):
            dp[j] += dp[j - i]
    return dp[n]




for i in range(1, 13):
    print(i, partition_dp(i, i))



# Using dynamic programming and generalised for any array                        
                                                                                 
