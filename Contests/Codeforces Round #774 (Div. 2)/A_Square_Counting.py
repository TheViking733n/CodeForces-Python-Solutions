import sys,os,io

# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
# input = sys.stdin.readline


TestCases = 1
TestCases = int(input())

for _ in range(TestCases):
    n,s = [int(i) for i in input().split()]
    # n = int(input())
    # arr = [int(i) for i in input().split()]
    # # s = input()

    n2 = n*n

    x = s//n2

    print(x)