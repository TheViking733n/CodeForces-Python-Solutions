import sys
input = sys.stdin.readline
print = lambda x: sys.stdout.write(str(x) + "\n")

import math
def solve():
    n = int(input())
    if n < 7:
        print("NO")
        return 
    if (n & (n + 1)) == 0:
        print("YES")
        return 
    for k in range(3, int(math.sqrt(n)) + 30):
        dum = n * (k - 1) + 1
        cnt = 0
        flag = 0
        while dum >= k:
            if dum % k != 0:
                flag = 1
                break
            dum //= k
            cnt += 1
        if dum == 1 and cnt > 2 and flag == 0:
            print("YES")
            return 
    print("NO")
for _ in range(int(input())): solve()
