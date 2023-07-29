import sys
input = sys.stdin.readline
print = lambda x: sys.stdout.write(str(x) + "\n")



def same(a):
    if a[0] == a[1] == a[2]:
        return a[0]
    return '.'

def solve():
    ans = "DRAW"
    v = []
    for _ in range(3):
        v.append(input())

    for i in range(3):
        if same(v[i]) != '.':
            ans = same(v[i])
        dum = v[0][i] + v[1][i] + v[2][i]
        if same(dum) != '.':
            ans = same(dum)

    dum = v[0][0] + v[1][1] + v[2][2]
    if same(dum) != '.':
        ans = same(dum)

    dum2 = v[0][2] + v[1][1] + v[2][0]
    if same(dum2) != '.':
        ans = same(dum2)

    print(ans)

for _ in range(int(input())):
    solve()