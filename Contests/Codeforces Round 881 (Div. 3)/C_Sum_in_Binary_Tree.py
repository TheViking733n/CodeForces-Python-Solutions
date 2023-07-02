import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    sm = n
    while n != 1:
        sm += n >> 1
        n >>= 1
    print(sm)