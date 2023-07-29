import sys
input = sys.stdin.readline
print = lambda x: sys.stdout.write(str(x) + '\n')

abc = [chr(i+97) for i in range(26)]

for _ in range(int(input())):
    n = int(input())
    v = -1
    for num in range(1, n+1):
        if n%num:
            v = num
            break
    take = abc[:v]
    take *= (n+len(take)) // len(take)
    print(''.join(take[:n]))

