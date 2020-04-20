A, B = (int(x) for x in input().split())

if A > 9 or B > 9:
    print(-1)
else:
    print(A*B)
