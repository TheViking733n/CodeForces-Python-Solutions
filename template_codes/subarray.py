# All contiguous subarrays of array

array = [1, 2, 3, 4, 5]

for i in range(0, len(array)):
    for j in range(i, len(array)):
        subarr = array[i:j+1]

        print(subarr)