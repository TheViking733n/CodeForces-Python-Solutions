for _ in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    arr.append(-arr[-1])
    last,ans = arr[0],0
    for i in range(1,len(arr)):
        if last*arr[i]>0:
            last = max(last, arr[i])
        else:
            ans += last
            last = arr[i]
    print(ans)
