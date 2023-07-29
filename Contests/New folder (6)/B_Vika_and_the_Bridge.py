import sys
input = sys.stdin.readline
print = lambda x: sys.stdout.write(str(x) + "\n")
oo = 1 << 30

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = [int(i) - 1 for i in input().split()]
    ind = [[] for _ in range(k)]
    for i in range(n):
        ind[a[i]].append(i)
    ans = [[oo, oo] for _ in range(k)]
    for i in range(k):
        if len(ind[i]) == 0:
            continue
        mn = [ind[i][0], n - ind[i][-1] - 1]
        for j in range(len(ind[i]) - 1):
            cur, nxt = ind[i][j], ind[i][j + 1]
            diff = nxt - cur - 1
            mn.append(diff)
            mn.remove(min(mn))
        ans[i] = mn
    aa = oo
    for fst, snd in ans:
        if fst == oo:
            continue
        fst, snd = max(fst, snd), min(fst, snd)
        v1 = fst >> 1
        aa = min(aa, max(v1, snd))
    print(aa)

        