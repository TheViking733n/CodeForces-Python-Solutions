import sys
input = sys.stdin.readline
print = lambda x: sys.stdout.write(str(x) + "\n")

'''
x1 + x2 + ... + xk = n - k
Ex. n = 15, k = 100
make a diameter of size 10, and plant 10
'''


N = int(2e5) + 5
triangular = [0] * N
for i in range(1, N):
    triangular[i] = triangular[i - 1] + i

def f(n):
    ...

for _ in range(int(input())):
    n, k = map(int, input().split())