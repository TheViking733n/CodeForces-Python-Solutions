"""
NOTE:This code will only work if c_index_arr[0] < b < c_index_arr[-1]
"""

b = 8
c_index_arr = [1,3,5,6,7,9,10]
first = 0
last = len(c_index_arr) - 1
while first < last-1:
    mid = (first + last)//2
    if c_index_arr[mid] > b:
        last = mid
    elif b > c_index_arr[mid]:
        first = mid

# print(first,mid,last)

print(f"No. of items greater than {b} in\n{c_index_arr} \nis {len(c_index_arr)-last}")