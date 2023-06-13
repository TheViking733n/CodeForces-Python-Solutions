from fractions import Fraction
for _ in range(int(input())):
    print()
    x1, y1, x2, y2, x3, y3, x4, y4 = [int(i) for i in input().split()]

    """
    m1 = (y2-y1) / (x2-x1)
    m2 = (y4-y3) / (x4-y4)

    m1 = m2
    => (y2-y1)*(x4-y4) = (y4-y3)*(x2-x1)

    y - y1 = m1(x - x1)
    c1 = y1 - m1 * x1
    c2 = y3 - m2 * x3
    """
    m1 = Fraction(y2-y1, x2-x1)
    m2 = Fraction(y4-y3, x4-x3)
    print(m1, m2)
    if m1 != m2:
        print("YES")
    else:
        c1 = y1 - m1 * x1
        c2 = y3 - m2 * x3
        print(c1, c2)
        if c1 == c2:
            print("YES")
        else:
            print("NO")