import sys
input = sys.stdin.readline

def minimize(arr):
    n = len(arr)
    s, d = n >> 1, n >> 2
    a2 = [len(i) for i in arr.split('0')]
    ans = 0
    for i in range(len(a2)):
        while d > 0 and a2[i] > 1:
            d -= 1
            a2[i] -= 2
            ans += 1
        if d == 0: break
    return ans + sum(a2)


def maximize(arr):
    n = len(arr)
    s, d = n >> 1, n >> 2
    if arr.count(1) <= s: return arr.count(1)
    ans = 0
    for i in range(n - 1):
        if d == 0: break
        if (arr[i], arr[i+1]) in ((1, 0), (0, 1), (0, 0)):
            ans += arr[i] | arr[i+1]          
            arr[i], arr[i+1] = -2, 2
            d -= 1

    for i in range(n-1):
        if d == 0: break
        if (arr[i], arr[i+1]) == (1, 1):
            arr[i], arr[i+1] = -2, 2
            d -= 1
            ans += 1

    return ans + sum(arr)

m, n = map(int, input().split())
mn = mx = 0
for i in range(m):
    b = input().rstrip()
    mn += minimize(b)
    mx += maximize([int(i) for i in b])
print(mn, mx)
