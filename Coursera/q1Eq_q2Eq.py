def Eq(a, b, c1, c2, n):
    for i in range(n+1):
        if i == 0:
            p1 = (a + c1) / 2
            p2 = (a + b * p1 + c2) / 2
        else:
            p1 = (a + b * p2 + c1) / 2
            p2 = (a + b * p1 + c2) / 2

    print("%0.2f %0.2f" % (p1, p2))


a, b, c1, c2, n = input().split(",")
Eq(int(a), float(b), int(c1), int(c2), int(n))
