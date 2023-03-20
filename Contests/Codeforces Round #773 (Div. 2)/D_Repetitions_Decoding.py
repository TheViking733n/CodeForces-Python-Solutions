import sys,os,io
# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
# input = sys.stdin.readline

possible = True

def solve(arr):
    global possible
    if not possible:
        return []
    
    half = len(arr)>>1
    if half == 0:
        return []
    if half == 1:
        if arr[0] == arr[1]:
            return list(arr)
        else:
            possible = False
            return []
    if half == 2:
        if arr[0] == arr[2] and arr[1] == arr[3]:
            return list(arr)
        
        elif arr[0] == arr[1] and arr[1] == arr[2]:
            return arr + arr
        
        elif arr[0] == arr[3] and arr[1] == arr[2]:
            return arr[:2] + [arr[2],arr[2]] + arr[2:]

        else:
            possible = False
            return []


    left = solve(arr[:half])
    if not possible:
        return []
    right = solve(arr[half:])
    return left + right


for _ in range (int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    
    cntd = {}
    

    for i in arr:
        if i in cntd:
            cntd[i] += 1
        else:
            cntd[i] = 1
    
    flag = 1
    for num in cntd:
        if cntd[num] &1 == 1:
            print(-1)
            flag = 0
            break
    
    if flag == 0:
        continue

    solved = []

    print(solve(arr))

