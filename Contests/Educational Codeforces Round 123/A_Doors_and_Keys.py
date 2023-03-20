import sys,os,io
# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
 
for _ in range (int(input())):
    # n = int(input())
    line = input()

    keys = []
    possible = 0
    for ch in line:
        if ch in "rgb":
            keys.append(ch)
        else:
            if ch.lower() in keys:
                possible = 1
            else:
                possible = 0
                break
    
    if possible:
        print("YES")
    else:
        print("NO")
