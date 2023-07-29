import sys
input = sys.stdin.readline
oo = 1 << 60

'''
Array is blue initially.

1. Choose any Blue ele and paint it red
        => cost 1
2. Choose Red ele != 0 and a blue ele adjacant to it
        => paint blue to red
        => decrease red by 1


B B B B B B B
0 1 0 0 1 0 2

B B B B B B R | cost = 1
0 1 0 0 1 0 2
            ^

B B B B B R R | cost = 1
0 1 0 0 1 0 1
          ^

B B B B R R R | cost = 2
0 1 0 0 1 0 1
        ^

B B B R R R R | cost = 2
0 1 0 0 1 0 1
      ^

B B R R R R R | cost = 3
0 1 0 0 1 0 1
    ^

B R R R R R R | cost = 4
0 1 0 0 1 0 1
  ^

R R R R R R R | cost = 4
0 0 0 0 1 0 1
^

'''

n = int(input())
arr = list(map(int, input().split()))
a2 = [arr[0]]
for i in arr[1:]:
    if i == 0 or a2[-1] != i:
        a2.append(i)
print(a2)

if len(a2) == 1:
    print(1)
    exit()

a3 = [[]]
for i in a2:
    if i == 0:
        a3.append([])
    else:
        a3[-1].append(i)
print(a3)

a4 = []
for i in a3:
    if i and 2 in i:
        a4.append(2)
    elif i:
        a4.append(1)
    a4.append(0)
a4.pop()
print(a4)

if len(a4) == 1:
    print(1)
    exit()

n = len(a4)
arr = a4
vis = [0] * n
ans = 0
for i in range(n):
    if arr[i] == 2:
        if i >= 1: vis[i-1] = 1
        if i < n - 1: vis[i+1] = 1
        vis[i] = 1
        ans += 1

for i in range(n):
    if arr[i] == 1:
        if i >= 1 and vis[i-1] == 0:
            vis[i-1] = 1
        elif i < n - 1:
            vis[i+1] = 1
        vis[i] = 1
        ans += 1

ans += vis.count(0)
print(ans)