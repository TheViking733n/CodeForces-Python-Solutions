# Refer - https://codeforces.com/blog/entry/7262

from collections import Counter

MAX_N = int(1e6) + 5
sp = [-1] * MAX_N  # Smallest prime of a number, for a prime p, sp[p] = p

def init_sp():
    for i in range(2, MAX_N, 2):
        sp[i] = 2    # For all even no., its sp will be 2
    
    for i in range(3, MAX_N, 2):  # Now for odd numbers
        if sp[i] == -1:
            sp[i] = j = i
            while j * i < MAX_N:
                if sp[j * i] == -1:
                    sp[j * i] = i
                j += 2

def factorize(n):
    ans = Counter()
    while n != 1:
        ans[sp[n]] += 1
        n //= sp[n]
    return ans



init_sp()
print(factorize(2**5 * 3**3 * 5**2))
