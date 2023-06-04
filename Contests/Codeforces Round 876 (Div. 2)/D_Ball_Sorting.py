import sys
input = sys.stdin.readline
# print = sys.stdout.write

def LIS(nums, cmp=lambda x, y: x < y):
    P = [0] * len(nums)
    M = [0] * (len(nums) + 1)
    L = 0

    for i in range(len(nums)):
        lo, hi = 1, L

        while lo <= hi:
            mid = (lo + hi) // 2
            if cmp(nums[M[mid]], nums[i]):
                lo = mid + 1
            else:
                hi = mid - 1

        newL = lo
        P[i] = M[newL - 1]
        M[newL] = i

        L = max(L, newL)

    S = [0] * L
    k = M[L]

    for i in range(L - 1, -1, -1):
        S[i], k = nums[k], P[k]

    return S



for _ in range(int(input())):
    print()
    n = int(input())
    arr = list(map(int, input().split()))
    print(LIS(arr))
    used = set(LIS(arr))
    b = [1] * n
    for i in range(n):
        if arr[i] in used:
            b[i] = 0
    
    print(b)
    if 1 not in b:
        print(*([0] * n))
        continue

    first1 = b.index(1)
    last1 = n - b[::-1].index(1) - 1
    if first1 == last1:
        print(*([1] * n))
        continue
    # print(first1, last1)
    cnt = []; prev = first1
    for i in range(first1+1, last1 + 1):
        # Counting no. of consecutive zeroes between two 1s
        if b[i] == 1:
            if i - prev - 1 > 0: 
                cnt.append(i - prev - 1)
            prev = i
    print(cnt)
    cnt.sort()
    ans = []
    cur = last1 - first1
    if b[0] == 1:
        cnt[0] -= 1
    if b.count(1) > 1 and b[-1] == 1:
        cnt[-1] -= 1
    if b[0] or b[1]:
        cur += 1
    for i in range(n):
        ans.append(cur)
        if cnt: cur -= cnt.pop()



    print("Ans:", *ans)


