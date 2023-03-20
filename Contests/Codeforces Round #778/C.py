from __future__ import division, print_function
import os,sys
from io import BytesIO, IOBase

if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip




from math import ceil, floor, factorial
# from math import log,sqrt,cos,tan,sin,radians
from bisect import bisect_left, bisect_right
from collections import defaultdict
# from collections import deque, Counter, OrderedDict
# from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace
# from bisect import bisect,bisect_left,bisect_right,insort,insort_left,insort_right
# from decimal import *

# from itertools import permutations

# ======================== Functions declaration Starts ========================


abc='abcdefghijklmnopqrstuvwxyz'
abd={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}


M=1000000007
# M=998244353
INF = float("inf")
PI = 3.141592653589793

def copy2d(lst): return [x[:] for x in lst]   #Copy 2D list... Avoid Using Deepcopy
def isPowerOfTwo(x): return (x and (not(x & (x - 1))) )

LB = bisect_left   # Lower bound
UB = bisect_right  # Upper bound
 
def BS(a, x):      # Binary Search
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    else:
        return -1

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return (x*y)//gcd(x,y)

# import threading
# def dmain():
#     sys.setrecursionlimit(1000000)
#     threading.stack_size(1024000)
#     thread = threading.Thread(target=main)
#     thread.start()
    
# ========================= Functions declaration Ends =========================


def rBS(arr, x):
    l = 0
    r = len(arr)-1
    ans = -1
    while l<=r:
        mid = (l+r)//2
        if arr[mid] == x:
            ans = mid
            break
        elif arr[mid] > x:
            l = mid+1
        else:
            r = mid-1
    # while ans>0 and arr[ans-1]==x:
    #     ans -= 1
    return ans


def main():
    TestCases = 1
    TestCases = int(input())

    for _ in range(TestCases):
        # n,k = [int(i) for i in input().split()]
        n = int(input())
        arr = [int(i) for i in input().split()]
        # b = arr[:]
        # s = input()
        
        
        if _ == 68:
            print(arr)
        else:
            continue

        if n==1:
            print("YES")
            continue
            
        elif n==2:
            if abs(arr[0]-arr[1])<=1:
                print("YES")
            else:
                print("NO")
            continue


        arr.sort(reverse=True)

        # g = gcd(arr[0], arr[1])

        # for i in range(n):
        #     g = gcd(g, arr[i])
        
        # if g>1:
        #     for i in range(n):
        #         arr[i] //= g

        


        # Special Case of power of 2

        # pow2 = []
        # temp = []
        
        # k = 1
        # while k <= 1000*1000*1000:
        #     if rBS(arr,k)!=-1:
        #         pow2.append(k)
        #     elif len(pow2)>0:
        #         break
        #     k <<= 1
        

        # Special case all are power of 2

        # f = 0
        # for num in arr:
        #     if not isPowerOfTwo(num):
        #         f = 1
        #         break
        
        # if f==0:













        # for d in arr:
        #     if isPowerOfTwo(d):
        #         pow2.append(d)
        #     else:
        #         temp.append(d)
        
        # arr = temp
        

        # if len(pow2)>2:

    
        # # arr2 = arr[:]
        # sm = arr[-1]
        # f = 1
        # for i in range(n-2,-1,-1):
        #     if abs(sm-arr[i])<=1:
        #         sm += arr[i]
        #     else:
        #         f = 0
        #         break

        # if f:
        #     print("YES")
        #     continue


        a2 = arr[:]


        f = 1
        while len(arr)>1:

            sm = arr[-1]
            ind = rBS(arr, sm+1)
            if ind == -1:
                # Not found
                if arr[-2]-arr[-1]<=1:
                    arr[-2] += arr[-1]
                    arr.pop()
                    arr.sort(reverse=True)
                else:
                    f = 0
                    break
            else:
                # First occurance of sm+1 is at ind


                arr[ind] += sm
                arr.pop()
                arr.sort(reverse=True)



        if f==-1: continue
        
        # b.sort(reverse=True)
        # print(b,"#",arr)
        
        if f:
            print('YES')
        else:

            # Trying again maybe its a power of 2 series
            arr = a2
            f = 1
            while len(arr)>1:

                if arr[-2]-arr[-1]<=1:
                    arr[-2] += arr[-1]
                    arr.pop()
                    arr.sort(reverse=True)
                else:
                    f = 0
                    break
            
            if f:
                print('YES')
            else:
                
                print('NO')
            
            
          
        
   
if __name__ == "__main__":
    #read()
    main()
    #dmain()

