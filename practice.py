import sys
input = sys.stdin.readline
 
for _ in range (int(input())):
    input()
    a = []
    for __ in range (8):
        a.append(list(input().strip()))
    ans = -1
    for i in range (8):
        cnt1 = 0
        cnt2 = 0
        for j in range (8):
            if a[i][j]=='R':
                cnt1+=1
            elif a[i][j]=='B':
                cnt2+=1
        if cnt1==8:
            ans = 'R'
    
    if ans != -1:
        print(ans)
        continue
 
    for j in range (8):
        cnt1 = 0
        cnt2 = 0
        for i in range (8):
            if a[i][j]=='R':
                cnt1+=1
            elif a[i][j]=='B':
                cnt2+=1
        if cnt2 == 8:
            ans = 'B'
    print(ans)
