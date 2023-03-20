import sys,os,io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
 
for _ in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    
    
    # arr = [2,9,6,7,10]

    # n = len(arr)

    even = []
    odd = []

    for i in range(n):
        if arr[i]%2==0:
            even.append(arr[i])
        else:
            odd.append(arr[i])

    if len(odd)==0:
        ev2 = even[:]
        ev2.sort()
        if (ev2 == even):
            print("YES")
        else:
            print("NO")
    
    elif len(even)==0:
        od2 = odd[:]
        od2.sort()
        if (od2 == odd):
            print("YES")
        else:
            print("NO") 
    
    else:
        ev2 = even[:]
        od2 = odd[:]
        ev2.sort()
        od2.sort()
        if (ev2 == even and od2 == odd):
            print("YES")
        else:
            print("NO")
            