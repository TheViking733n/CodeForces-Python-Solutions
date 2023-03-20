import sys,os,io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
 
for _ in range (int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    cnd = ans = cnd2 = 0
    # print(arr[1:-1])
    for num in arr[1:-1]:
        if num%2==0:
            half = num//2
            if cnd<0:
                cnd+=min(-cnd, half)
            cnd+=half
            ans += half
        else:
            cnd-=1
            ans += (num+1)//2
    for i in range(n-2,0, -1):
        num = arr[i]
        if num%2==0:
            half = num//2
            if cnd2<0:
                cnd2+=min(-cnd2, half)
            cnd2+=half
        else:
            cnd2-=1

    
    if (cnd<0 or cnd2<0):
        ans = -1
    
    print(ans)
