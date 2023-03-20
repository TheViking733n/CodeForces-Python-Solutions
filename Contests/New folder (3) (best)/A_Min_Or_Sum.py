import sys,os,io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
 
for _ in range (int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    mx = max(arr)
    bit = 1
    sum = 0
    cnt = 0
    while cnt < 30:
        for num in arr:
            if num&bit == bit:
                sum += bit
                break
        bit <<= 1
        cnt +=1
        if bit>mx:
            break
    
    print(sum)

