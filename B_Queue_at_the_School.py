import sys
input = sys.stdin.readline
n, k = [int(i) for i in input().split()]
s = input()
ans = ['B'] * n
ans[0] = s[0]
occupied = -1 if s[0] == 'B' else 0
shift = k
for i in range(1, n):
    if s[i] == 'B':
        shift = k
        continue
    newPos = i - shift
    if newPos <= occupied:
        occupied += 1
        ans[occupied] = 'G'
    else:
        ans[newPos] = 'G'
        occupied = newPos
    shift -= 1
print(''.join(ans))
