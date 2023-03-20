import sys,os,io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def solve(n, rank):
    cnt = 0
    x,y = 0,1
    for i in range(1,n):
        for j in range(i):
            cnt+=1
            if cnt==rank:
                x,y=i,j
                break
        if cnt==rank:
            break
    
    arr=['a']*n
    arr[-x-1]='b'
    arr[-y-1]='b'

    print("".join(arr))



for _ in range(int(input())):
    n,r = [int(i) for i in input().split()]
    solve(n,r)
