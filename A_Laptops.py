# n, mx = int(input()), 0
# arr = sorted(list(map(int, input().split())) for _ in range(n))
# for _, y in arr:
#     if y < mx: exit(print('Happy Alex'))
#     mx = y
# print('Poor Alex')

print(("Poor","Happy")[any((lambda x,y:x!=y)(*input().split())for _ in range(int(input())))],"Alex")