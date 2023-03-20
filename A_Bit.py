import sys,os,io
# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
# input = sys.stdin.readline
 
for _ in range(1):
    n = int(input())
    cnt = 0
    for x in range(n):
        s = input()
        if '++' in s:
            cnt += 1
        else:
            cnt -= 1
    
    print(cnt)
