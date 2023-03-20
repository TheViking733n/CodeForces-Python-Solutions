import sys,os,io
from bisect import bisect_left
from bisect import bisect_right

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
# input = sys.stdin.readline
 
LB = bisect_left
UB = bisect_right

def BS(a, x):    # Binary search
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    else:
        return -1


for _ in range (int(input())):
    n, l, r= [int(i) for i in input().split()]
    arr = [int(i) for i in input().split()]
    arr.sort()

    left, right = 0, n-1

    cnt = 0

    for i in range(n-1):
        cur = arr[i]
        ind1 = LB(arr, l-cur, lo=i+1)
        ind2 = UB(arr, r-cur, lo=i+1)
        
        cnt += ind2 - ind1


    print(cnt)