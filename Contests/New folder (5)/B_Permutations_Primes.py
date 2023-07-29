import sys
input = sys.stdin.readline
print = lambda x: sys.stdout.write(str(x) + '\n')

for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(1)
        continue
    if n == 2:
        print("2 1")
        continue
    if n == 3:
        print("2 1 3")
        continue

    ans = [-1] * n
    ans[0] = 2
    ans[-1] = 3
    ans[n>>1] = 1
    cnt = 4
    for i in range(n):
        if ans[i] == -1:
            ans[i] = cnt
            cnt += 1
    print(' '.join(map(str, ans)))