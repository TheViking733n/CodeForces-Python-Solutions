import sys,os,io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
 
for _ in range (int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    ans = 0
    zeros = []
    for i in range(n):
        if arr[i]==0:
            zeros.append(i)
        
    for i in range(n):
        for j in range(i+1, n+1):
            # print(arr[i:j])
            ans+=len(arr[i:j])
            for ind in zeros:
                if i<=ind<j:
                    ans+=1
                elif ind>=j:
                    break
    print(ans)