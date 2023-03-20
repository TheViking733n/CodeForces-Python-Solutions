# Kadane's Algorithm
arr = [-2, 1, -3, 4, -1, 2, 1, 8, -5, 4]
n = len(arr)

mx = curmax = arr[0]
for i in range(1, n):
    curmax = max(arr[i], curmax + arr[i])
    mx = max(mx, curmax)

mx = max(0, mx)  # SPECIAL CASE: If all elements -ve, take none

print(mx)






# Kadane's Algorithm with index
arr = [-2, 1, -3, 4, -1, 2, 1, 8, -5, 4]
n = len(arr)

mx = curmax = arr[0]
start = end = prev_start = 0
for i in range(1, n):
    if arr[i] > arr[i] + curmax:
        curmax = arr[i]
        prev_start = i
    else:
        curmax = curmax + arr[i]
    
    if curmax > mx:
        mx = curmax
        start = prev_start
        end = i

if mx<0:   # SPECIAL CASE: If all elements -ve, take none
    mx = 0
    start = end = -1

print(mx, start, end, arr[start:end+1])
