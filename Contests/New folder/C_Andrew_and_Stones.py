import sys,os,io
# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
 
for _ in range (int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    
    ans = 0

    odd = []
    for i in range(1,n-1):
        num = arr[i]
        if num%2 == 0:
            ans += num//2
        else:
            ans += (num+1)//2
            odd.append(i)
    
    for i in range(1,n-1):
        num = arr[i]
        while (num>1):
            for j in range(len(odd)):
                ind = odd[j]
                if ind < i:
                    odd.remove(ind)
                    break
                
            for j in range(len(odd)-1, 0, -1):
                ind = odd[j]
                if ind > i:
                    odd.remove(ind)
                    break
        
    if len(odd)>0:
        ans += 1
        
    print(ans)
