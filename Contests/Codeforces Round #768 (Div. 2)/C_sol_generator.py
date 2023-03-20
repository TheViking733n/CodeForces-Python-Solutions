from itertools import permutations


def print_sol(n, k):  # n must be power of 2
    
    arr = list(range(n))

    all_perm = list(permutations(arr))
    # print(all_perm)



    for k in range(n):
        for perm in all_perm:
            sum = 0
            for i in range(0, len(perm), 2):
                a, b = perm[i], perm[i+1]
                sum += a&b
            
            if (sum == k):
                print(f"{(n, k)} =>\t{perm}")
                break

        else:
            print(f"{(n, k)} =>\tNo possible solution found")



def print_all_sol(n):  # here k will vary from 0 to n-1
    
    arr = list(range(n))

    all_perm = list(permutations(arr))
    # print(all_perm)

    for k in range(n):
        for perm in all_perm:
            sum = 0
            for i in range(0, len(perm), 2):
                a, b = perm[i], perm[i+1]
                sum += a&b
            
            if (sum == k):
                print(f"{(n, k)} =>\t{perm}")
                break

        else:
            print(f"{(n, k)} =>\tNo possible solution found")




for pow in range(1, 4):  # for pow = 4 system crashes coz it takes more than 10 gigs of ram
    print_all_sol(2**pow)
    print()

