import sys,os,io
# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
# input = sys.stdin.readline
def main():
    TestCases = 1
    TestCases = int(input())

    for _ in range(TestCases):
        _ = input()
        k, n, m = [int(i) for i in input().split()]
        # n = int(input())
        A = [int(i) for i in input().split()]
        B = [int(i) for i in input().split()]

        i = j = 0

        ans = []
        possible = True

        while i < n or j < m:
            if i<n and A[i] == 0:
                ans.append(A[i])
                i += 1
                k+=1
            elif j<m and B[j] == 0:
                ans.append(B[j])
                j += 1
                k+=1
            elif i<n and A[i] <= k:
                ans.append(A[i])
                i += 1
            elif j<m and B[j] <= k:
                ans.append(B[j])
                j += 1
            else:
                possible = False
                break
        
        if possible:
            print(*ans)
        else:
            print("-1")
             
            
main()