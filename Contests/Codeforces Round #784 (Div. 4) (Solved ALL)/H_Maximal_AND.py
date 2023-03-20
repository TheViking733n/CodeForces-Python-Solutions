TestCases = int(input())

for _ in range(TestCases):
    n,k = [int(i) for i in input().split()]
    arr = [int(i) for i in input().split()]
    
    cnt = [0]*31
    for j in range(31):
        slider = 1<<j
        for i in range(n):
            if arr[i]&slider:
                cnt[j]+=1
    
    # print(cnt[:5],cnt[-3:])
            
    for j in range(30,-1,-1):
        req = n - cnt[j]
        if k >= req:
            k-=req
            cnt[j] = n

        if k<=0:
            break
    
    # print(cnt[:6], cnt[-3:], k)

    ans = 0
    pow = 1
    for i in range(31):
        ans += pow if cnt[i]==n else 0
        pow = pow<<1

    print(ans)