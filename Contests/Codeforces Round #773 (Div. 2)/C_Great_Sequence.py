import sys,os,io
from bisect import bisect_left
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
# input = sys.stdin.readline
 
def BS(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    else:
        return -1


 
for _ in range (int(input())):
    n,x = [int(i) for i in input().split()]
    arr = [int(i) for i in input().split()]
    arr.sort()

    ans =0

    for i in range(n):
        if arr[i] == -1:
            continue
        req = arr[i]*x
        ind = BS(arr, req)
        if  ind != -1:
            arr[i]=-1
            arr[ind]=-1
            
        else:
            ans += 1
        
    
    print(ans)