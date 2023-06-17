import sys
input = sys.stdin.readline

'''
Count no. of distinct elements in an array
'''

n = int(input())
arr = [int(i) for i in input().split()]

# arr.sort()
arr = set(arr)
print(len(arr))

