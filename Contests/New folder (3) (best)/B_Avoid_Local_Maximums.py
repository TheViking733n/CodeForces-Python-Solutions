import sys,os,io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
 
for _ in range (int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]

    if n==2:
        print(0)
        print(arr[0],arr[1])
    
    else:
        ans = 0
        last = -1
        for i in range(1,n-1):
            if arr[i-1]<arr[i] and arr[i]>arr[i+1]:
                
                if (i+2)<(n-1) and arr[i+2]>arr[i+1] and arr[i+2]>arr[i+3]:
                    ans += 1
                    arr[i+1] = max(arr[i],arr[i+2])
                    
                else:
                    ans += 1

                    arr[i+1] = arr[i]
            
        print(ans)
        print(*arr)
        