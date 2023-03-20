for _ in range(int(input())):
    # n,k = [int(i) for i in input().split()]
    n = int(input())
    arr = [int(i) for i in input().split()]
    # s = input()
    mx = max(arr)

    answers = []
    for j in range(2):
        diff = [mx-i+j for i in arr]

        # print(diff)
        c1 = 0
        for i in range(n):
            if diff[i]&1:
                c1+=1
                diff[i]-=1
        
        diff.sort(reverse=True)

        sm = sum(diff)
        c2 = sm//2
        # print(diff,c1,c2)

        if c1>c2:
            ans = c1*2-1
        
        elif c1+1==c2 or c1==c2:
            ans = c2*2

        else:
            total = c1 + c2*2
            q, r = total//3, total%3
            c1, c2 = q+r-2, q+1
            
            while c1<c2-1:
                c1+=2
                c2-=1
        
            if c1>c2:
                ans = c1*2-1
            
            elif c1+1==c2 or c1==c2:
                ans = c2*2
        # print(c1,c2)
        answers.append(ans)

    print(min(answers))
