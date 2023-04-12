import os,sys
from itertools import combinations
input = sys.stdin.buffer.readline 
INF = int(1e18)
def main():
    TestCases = 1
    TestCases = int(input())
    
    for _ in range(TestCases):
        n, k = [int(i) for i in input().split()]
        
        a = [ord(i) - 97 for i in input().decode().strip()]
        b = [ord(i) - 97 for i in input().decode().strip()]


        taken = [0] * 26
        for i in a:
            taken[i] = 1
        chars = [i for i in range(26) if taken[i]]

        if len(chars) <= k:
            print(n * (n + 1) >> 1)
            continue
        
        ans = -INF
        for comb in combinations(chars, k):
            sm = cur = 0
            chosen = [0] * 26
            for ch in comb:
                chosen[ch] = 1
            for i in range(n):
                v = chosen[a[i]] or a[i] == b[i]
                cur += 1; cur *= v
                sm += cur
            ans = max(ans, sm)
        
        sys.stdout.write(f'{ans}\n')
        


if __name__ == "__main__":
    #read()
    main()
    #dmain()
