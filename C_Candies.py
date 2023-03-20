import sys
input = sys.stdin.readline

from math import gcd, lcm    # Use gcd(*arr) to pass a list
import bisect

for _ in range (int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    s = [set() for i in range (32)]
    f = 0
    for i in range (n):
        f|= a[i]
        bi = bin(a[i])[2:][::-1]
        for j in range (len(bi)):
            if bi[j]=='1':
                s[j].add(a[i])
    ans = [max(a)]
    rem = f^ans[0]
    
    for x in range (31, -1, -1):
        cur = -1
        for k in range (31,-1,-1):
            if ((rem>>k)&1):
                if cur==-1:
                    cur = s[k]
                else:
                    ncur = cur.intersection(s[k])
                    if len(ncur)==0:
                        continue
                    cur = ncur
        if cur!=-1:
            ans.append(cur.pop())
            for k in range (31, -1, -1):
                if ((rem>>k)&1) and ((ans[-1]>>k)&1):
                    rem^=(1<<k)
    done = {}
    for i in ans:
        done[i]=1
    for i in a:
        if i in done and done[i]==1:
            done[i]-=1
        else:
            ans.append(i)
    print(*ans)