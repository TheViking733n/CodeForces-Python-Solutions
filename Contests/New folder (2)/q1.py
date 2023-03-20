import sys,os,io
# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
 
for _ in range (int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]

    if (n==1):
        print(arr[0])
        
    elif (n==2):
        print(min(arr[0],arr[1]), max(arr[0],arr[1]))
        
    else:
        val = 1
        ans = -1
        for i in range(n):
            if arr[i] == val:
                val += 1
            else:
                end = arr.index(val, i)
                # print(end)
                # print(arr[:i], arr[i:end+1][::-1],  arr[end+1:])
                ans = arr[:i] + arr[i:end+1][::-1] + arr[end+1:]
                print(*ans)
                break
        if ans == -1:
            print(*arr)
