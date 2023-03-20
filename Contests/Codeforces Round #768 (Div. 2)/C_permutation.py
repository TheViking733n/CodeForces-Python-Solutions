from itertools import permutations

arr = list(range(1))

all_perm = list(permutations(arr))
# print(all_perm)

all_perm = [list(range(8))]

k = 4

for perm in all_perm:
    sum = 0
    for i in range(0, len(perm), 2):
        a, b = perm[i], perm[i+1]
        sum += a&b
    
    if (sum == k):
        print(perm)
        break

else:
    print("No possible solution found")
