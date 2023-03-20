import sys,os,io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
 
for _ in range (int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]

    if arr[-2] > arr[-1]:
        print(-1)
    
    else:
        diff = arr[-2] - arr[-1]

        if arr[-3] > arr[-2] and diff > arr[-2]:
            print(-1)
            continue

        if diff <= arr[-2]:
            # easy
            print(n-2)
            for i in range(1, n-1):
                print(i, n-1, n)
        
        else:
            # Critical
            mx = max(arr[:-2])
            if mx > arr[-2]:
                print(-1)

            else:
                sorted = True
                for x in range(n-1):
                    sorted = arr[x] <= arr[x+1]
                    if not sorted:
                        break
                    
                if sorted:
                    print(0)
                else:
                    print(-1)


