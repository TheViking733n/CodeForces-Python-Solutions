import sys
input = sys.stdin.readline
print = lambda x: sys.stdout.write(str(x) + '\n')
from collections import defaultdict

for _ in range(int(input())):
    n, m, k = map(int, input().split())
    lines = []
    for _ in range(k):
        x1, y1, x2, y2 = [int(i) for i in input().split()]
        slope = (y2 - y1) / (x2 - x1)
        if slope > 0: slope = 1
        else: slope = -1
        center = (x1 + x2, y1 + y2, slope)
        lines.append(center)
    lines.sort()
    ok = True
    for i in range(len(lines)-1):
        x1, y1, s1 = lines[i]
        x2, y2, s2 = lines[i+1]
        if x1 == x2 and y1 == y2 and s1 != s2:
            ok = False
            break
    if not ok:
        print("NO")
        continue
    
    # print(lines)
    ln = len(lines)
    slope = defaultdict(int)
    for x, y, s in lines:
        slope[(x, y)] = s
    for i in range(ln - 1):
        for j in range(i + 1, ln):
            x1, y1, s1 = lines[i]
            x2, y2, s2 = lines[j]
            if x1 == x2 or y1 == y2: continue
            s3, s4 = slope[(x1, y2)], slope[(x2, y1)]
            if s3 == 0 or s4 == 0: continue
            # print((s1, s2, s3, s4))
            if abs(s1 + s2 + s3 + s4) == 2:
                ok = False
                break
        if not ok: break
    print('YES' if ok else 'NO')

    # g = defaultdict(list)
    # for x, y, s in lines:
    #     g[x].append((y, s))
    # for k, row in g.items():
    #     row.sort()

    # xx = list(g.keys())
    # for i in range(len(xx) - 1):
    #     for j in range(i + 1, len(xx)):



    