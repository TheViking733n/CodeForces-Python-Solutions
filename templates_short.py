import sys,os,io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

TestCases = 1
TestCases = int(input())

for _ in range(TestCases):
    # n,x,y = [int(i) for i in input().split()]
    n = int(input())
    arr = [int(i) for i in input().split()]
    # s = input()
    