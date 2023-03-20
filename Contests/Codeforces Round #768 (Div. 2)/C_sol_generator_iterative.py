def permutations(s):
 
    if not s:
        return []
 
    partial = []
 
    partial.append(s[0])

    for i in range(1, len(s)):

        for j in reversed(range(len(partial))):

            curr = partial.pop(j)
 
            for x in range(len(curr) + 1):
                perm = s[0] + curr[:x] + s[i] + curr[x:]
                partial.append(curr[:x] + s[i] + curr[x:])
            
            print(partial[j])
    print(partial)        

def print_all_sol(n):  # here k will vary from 0 to n-1
    
    arr = list(range(n))

    all_perm = list(permutations(arr))
    # print(all_perm)

    for k in range(n):
        for perm in all_perm:
            sum = 0
            for i in range(0, len(perm)//2, 2):
                a, b = perm[i], perm[i+1]
                sum += a&b
            
            if (sum == k):
                print(f"{(n, k)} =>\t{perm}")
                break

        else:
            print(f"{(n, k)} =>\tNo possible solution found")




# for pow in range(1, 5):
#     print_all_sol(2**pow)
#     print()

permutations("123")