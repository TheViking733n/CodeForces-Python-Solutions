import sys
input = sys.stdin.readline
print = lambda x: sys.stdout.write(str(x) + "\n")

for _ in range(int(input())):
    ans = 0
    for i in range(int(input())):
        a, b = map(int, input().split())
        if a > b:
            ans += 1
    print(ans)
    