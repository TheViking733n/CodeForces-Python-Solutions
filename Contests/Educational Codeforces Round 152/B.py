from itertools import combinations

def solve(arr, k):
    abc = 'abcdefghij'
    ans = 0
    for p in combinations(abc, k):
        cnt = 0
        for word in arr:
            cnt += all(c in p for c in word)
        ans = max(ans, cnt)
    return ans
    

def solve(arr, k):
    return max(sum(all(c in p for c in word) for word in arr) for p in combinations('abcdefghij', k))
    