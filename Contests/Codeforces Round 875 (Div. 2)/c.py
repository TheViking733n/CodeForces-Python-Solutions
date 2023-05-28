from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    arr = []
    for _ in range(n-1):
        arr.append(tuple(int(i)-1 for i in input().split()))
    
    ind = []
    for i in range(n):
        ind.append(1 << 30)
    ind[0] = 0
    for i in range(n-1):
        u, v = arr[i]
        ind[u] = min(ind[u], i)
        ind[v] = min(ind[v], i)
    print(ind)

        