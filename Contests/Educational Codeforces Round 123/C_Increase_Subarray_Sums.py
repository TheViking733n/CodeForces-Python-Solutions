from audioop import reverse
import sys,os,io
# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
 
for _ in range (int(input())):
    n, k = [int(i) for i in input().split()]
    arr = [int(i) for i in input().split()]

    if n==1:
        print(max(arr[0], 0), max(arr[0]+2,0))


    mx = max(arr)
    mn = min(arr)
    if mn>0:
        print(sum(arr), end=" ")
    elif mx<0:
        print(0, end=" ")
    else:
        print(mx, end=" ")
    
    groups = [[arr[0]]]
    for i in range(1, n):
        num  = arr[i]
        sign1 = num>=0
        sign2 = groups[-1][-1]>=0

        if sign1==sign2:
            groups[-1].append(num)
        else:
            groups.append([num])
    
    # print(*groups, sep="  ")


    start_ind = int(groups[0][0]<0)

    positive = {}

    for i in range(start_ind, len(groups), 2):
        g = groups[i]
        l = len(g)
        if l in positive:
            tup = (sum(g),i)
            positive[l].append(tup)
            positive[l].sort(reverse=True)
        else:
            tup = (sum(g),i)
            positive[l] = [tup]
    
    # print(positive)

    negative = {}

    start_ind = int(groups[0][0]>=0)

    for i in range(start_ind, len(groups), 2):
        g = groups[i]
        l = len(g)
        if l in negative:
            tup = (sum(g),i)
            negative[l].append(tup)
            negative[l].sort(reverse=True)
        else:
            tup = (sum(g),i)
            negative[l] = [tup]

    # print(negative)
    last = 0
    maxg = 0 if positive=={} else max(positive.keys())
    for i in range(1, n+1):
        if i in positive:
            tup = positive[i][0]
            s = tup[0] + k*i
        
        elif i < maxg:
            for j in range(i+1, n+1):
                if j in positive:
                    tup = positive[j][0]
                    s = tup[0] + k*i
                    break
            
        else:
            left = i-maxg

            if left in negative:
                tup = negative[left][0]
                indg = tup[1]
                subg = groups[indg-1:indg+2]
                s = k*i
                for g in subg:
                    s += sum(g)




        
        ans = max(s, last)
        print(ans, end=" ")
        last = ans


    print()  

