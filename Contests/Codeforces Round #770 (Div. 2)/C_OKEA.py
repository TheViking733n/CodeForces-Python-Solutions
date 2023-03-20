import sys,os,io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
 
for _ in range (int(input())):
    n,k = [int(i) for i in input().split()]

    if k==1:
        print("YES")
        for i in range(1,n+1):
            print(i)
        
    # elif k==2:
    #     print("YES")
    #     for i in range(1,n+1):
    #         print(i, n+i)
    
    elif n&1==0:
        print("YES")
        for i in range(1,n+1):
            for j in range(k):
                print(i + n*j, end=' ')
            print()



    else:
        print("NO")
    