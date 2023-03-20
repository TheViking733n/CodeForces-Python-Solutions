import os
import sys
from io import BytesIO, IOBase

from bisect import bisect_left, bisect_right
from math import ceil, floor


# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
# input = sys.stdin.readline


# ======================== Functions declaration Starts ========================

LB = bisect_left
UB = bisect_right
 
def BS(a, x):    # Binary Search
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    else:
        return -1

# ========================= Functions declaration Ends =========================


def contains(i,j):
    print("?", i+1, j+1)
    sys.stdout.flush()
    inp = input()
    if inp == "": inp = input()
    arr = [int(i)-1 for i in inp.split()]
    cnt = 0
    for x in arr:
        if i<=x<=j:
            cnt += 1
    return (j-i+2+cnt)&1

    




TestCases = 1
TestCases = int(input())

for _ in range(TestCases):
    inp = input()
    if inp == "": inp = input()
    n = int(inp)
    
    i = 0
    j = n-1
    # if (j-i+1)&1: j += 1
    # f(i,j,n)

    while i<j-1:
        mid = (i+j+1)//2
        # if (mid-i+1)&1:
        #     mid -= 1
        
        if contains(i,mid):
            j = mid
        else:
            i = mid + 1
    
    # print(i+1,j+1)
    if j - i < 1:
        print("!", i)
        sys.stdout.flush()
    else:
        print("?", i+1, j+1)
        sys.stdout.flush()
        inp = input()
        if inp == "": inp = input()
        arr = [int(i)-1 for i in inp.split()]
        if arr[0]==i:
            print("!", i)
            sys.stdout.flush()
        else:  
            print("!", j)
            sys.stdout.flush()
