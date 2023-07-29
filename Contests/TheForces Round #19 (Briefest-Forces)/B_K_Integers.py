import sys
input = sys.stdin.readline
print = lambda x: sys.stdout.write(str(x) + "\n")

N = int(1e5) + 5
spf = [i for i in range(N)]
for i in range(4, N, 2):
    spf[i] = 2
for i in range(3, int(N ** 0.5) + 1, 2):
    if spf[i] == i:
        for j in range(i * i, N, i):
            if spf[j] == j:
                spf[j] = i

for _ in range(int(input())):
    n, k = map(int, input().split())
    if spf[n] == n:
        print('NO')
    else:
        other = max(spf[n], n // spf[n])
        print('YES' if other >= k else 'NO')