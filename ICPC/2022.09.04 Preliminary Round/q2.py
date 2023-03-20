n = 10

odds = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            for l in range(1, n+1):
                a = [i, j, k, l]
                a.sort()
                odds += (a[1] + a[2]) % 2

print(odds)