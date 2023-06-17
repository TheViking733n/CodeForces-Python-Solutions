for _ in range(int(input())):
    p, q, _ = map(int, input().split())
    print([-1, 1][p*q<=0] * (abs(q) // abs(p)))
