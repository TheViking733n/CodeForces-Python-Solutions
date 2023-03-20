from itertools import permutations


def calc_xor_sum(array):
    sum = 0
    xor_arr = []
    for i in range(len(array)-1):
        print(f"{array[i]} ^ {array[i+1]}\t=  {array[i]^array[i+1]}")
        xor_arr.append(array[i]^array[i+1])

    return max(xor_arr)


for n in range(2,1):
    arr = list(range(n))

    all_perm = permutations(arr)

    min_sum = 100000000000000
    ans = None

    for perm in all_perm:
        # print(perm)
        sum = calc_xor_sum(perm)
        
        if min_sum > sum:
            min_sum = sum
            ans = perm


    print(n, min_sum, "-->", ans, sep = "\t")



tup = (4, 6, 3, 2, 0, 8, 9, 1 ,7 ,5)

tup = (0, 1, 3, 4, 5, 6, 7, 2, 10, 8, 9)

# tup = (5, 4, 6, 7, 3, 2, 0, 1, 9, 8, 10)

print(calc_xor_sum(tup))