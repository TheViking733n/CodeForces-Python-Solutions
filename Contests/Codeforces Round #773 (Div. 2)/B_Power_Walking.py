import sys,os,io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
# input = sys.stdin.readline
 
for _ in range (int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    
    cntd = {}
    sm = sum(arr)

    for i in arr:
        if i in cntd:
            cntd[i] += 1
        else:
            cntd[i] = 1
    
    # nums = [] # (number, count)

    # for k in cntd:
    #     nums.append((cntd[k], k))
    
    # nums.sort()

    # distn = len(nums)
    # distn = cntd[arr[0]]
    # for num in cntd:
    #     if cntd[num] > distn:
    #         distn = cntd[num]

    distn = len(cntd)

    left = distn - n +1

    print(f"{distn} "*(distn-1), end ="")


    print(*list(range(distn, n+1)))



