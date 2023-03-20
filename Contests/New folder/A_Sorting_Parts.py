import sys,os,io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
 
for _ in range (int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    arr2 = list(arr)
    arr.sort()
    if arr==arr2:
        print("NO")
    else:
        print("YES")