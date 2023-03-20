import sys,os,io
# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
 
for _ in range (int(input())):
    n,x,y = [int(i) for i in input().split()]
    arr = [int(i) for i in input().split()]
    
    alice = x
    bob = x+3

    