import sys
input = sys.stdin.readline
print = lambda x: sys.stdout.write(str(x) + '\n')

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    if sum(i>=0 for i in arr) == 0:
        print(max(arr))
        continue

    od = sum(i for i in arr[0:n:2] if i >= 0)
    ev = sum(i for i in arr[1:n:2] if i >= 0)
    print(max(od, ev))
    
