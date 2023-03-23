n = int(input())
p = [[' ']*(2*n-1) for _ in range(2*n-1)]
D,d = [n-1]*8, [-1,-1,1,1,1,-1,-1,1]
for i in range(n):
    for j in range(4):
        p[D[j]][D[j+4]] = '*'
        D[j] -= d[(4*(i>=n//2)+j-1)&7]
        D[j+4] += d[4*(i>=n//2)+j]
print(*[' '.join(p[i]).rstrip() for i in range(2*n-1)],sep='\n')