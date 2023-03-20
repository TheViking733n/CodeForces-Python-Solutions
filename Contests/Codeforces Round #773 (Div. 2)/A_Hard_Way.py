import sys,os,io
# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
# input = sys.stdin.readline
 
for _ in range (int(input())):
    # n = int(input())
    x1, y1 = [int(i) for i in input().split()]
    x2, y2 = [int(i) for i in input().split()]
    x3, y3 = [int(i) for i in input().split()]

    # if (x1 == x2 or x2 == x3 or x1==x3) and (y1==y2 or y2==y3 or y1==y3):
    #     if x1==x2:
    #         cx1 = x1
    #         cx2 = x3
    #     elif x2==x3:
    #         cx1 = x2
    #         cx2 = x1
    #     else:
    #         cx1 = x1
    #         cx2 = x2
        
    #     if y1==y2:
    #         cy1 = y1
    #         cy2 = y3
    #     elif y2==y3:
    #         cy1 = y2
    #         cy2 = y1
    #     else:
    #         cy1 = y1
    #         cy2 = y2
    
    # elif x1 == x2 or x2 == x3 or x1==x3:
    #     ...
    
    ans = 0
    if y1==y2 and y1>y3:
        ans += abs(x2-x1)

    elif y2==y3 and y2>y1:
        ans += abs(x2-x3)

    elif y1==y3 and y1>y2:
        ans += abs(x1-x3)
    
    print(ans)

    