import sys
input = sys.stdin.readline
oo = 1 << 60

'''
101100
  ^

'''

def nextGreaterElementIndex(arr, n):
    stack = []
    ans = [0] * n
    for i in range(n - 1, -1, -1):
        while stack and arr[i] >= arr[stack[-1]]:
            stack.pop()
        if stack:
            ans[i] = stack[-1]
        else:
            ans[i] = n
        stack.append(i)
    return ans

def prevSmallerElementIndex(arr, n):
    stack = []
    ans = [0] * n
    for i in range(n):
        while stack and arr[i] <= arr[stack[-1]]:
            stack.pop()
        if stack:
            ans[i] = stack[-1]
        else:
            ans[i] = -1
        stack.append(i)
    return ans

for _ in range(int(input())):
    n, m = map(int, input().split())
    s = input().strip()
    seen = set()
    nge = nextGreaterElementIndex(s, n)
    pse = prevSmallerElementIndex(s, n)
    for _ in range(m):
        l, r = [int(x) - 1 for x in input().split()]
        l1 = nge[l] if s[l] == '0' else l
        r1 = pse[r] if s[r] == '1' else r
        if l1 > r1: l1 = r1 = n
        seen.add((l1, r1))
    print(len(seen))