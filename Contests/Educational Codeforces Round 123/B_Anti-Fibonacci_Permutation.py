import sys,os,io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
 
for _ in range (int(input())):
    n = int(input())
    arr = list(range(n, 0, -1))
    cnt = 1
    print(*arr)

    if n==3:
        print(1,3,2)
        print(3,1,2)
        continue

    i = 1
    while i<n:
        arr[i-1], arr[i] = arr[i], arr[i-1]
        if (i*2-1==n):
            arr[0], arr[i] = arr[i], arr[0]
            print(*arr)
            arr[0], arr[i] = arr[i], arr[0]

        else:
            print(*arr)
        i += 1
        cnt += 1

