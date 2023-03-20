import sys,os,io

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
# input = sys.stdin.readline


TestCases = 1
TestCases = int(input())

for _ in range(TestCases):
    # n,x,y = [int(i) for i in input().split()]
    n = int(input())
    arr = [int(i) for i in input().split()]
    # s = input()

    arr.sort()








    s1 = arr[0] + arr[1]
    s2 = arr[n-1]

    i,j = 2,n-2

    possible = s1<s2

    while i<j:
        if possible:
            break
        
        s1+=arr[i]
        s2+=arr[j]
        i+=1
        j-=1
        possible = s1<s2

    
    # print(s1,s2)


    if s1<s2:
        print("YES")
    else:
        print("NO")