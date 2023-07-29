import sys
input = sys.stdin.readline
print = lambda x: sys.stdout.write(str(x) + "\n")


for _ in range(int(input())):
    n, m, h = map(int, input().split())
    scores = []
    for i in range(n):
        time = list(map(int, input().split()))
        time.sort()
        pen = tot = sol = 0
        for t in time:
            tot += t
            if tot > h: break
            pen += tot
            sol += 1
        scores.append((-sol, pen, i + 1))
    scores.sort()
    rank = None
    for i in range(n):
        if scores[i][2] == 1:
            rank = i + 1
            break
    print(rank)
