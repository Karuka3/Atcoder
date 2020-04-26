A, B, C, D = (int(x) for x in input().split())

while A > 0 and C > 0:
    C = C - B
    A = A - D
    if C <= 0:
        print("Yes")
        break
    else:
        if A <= 0:
            print("No")
            break
