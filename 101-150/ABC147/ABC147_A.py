A, B, C = (int(x) for x in input().split())
ans = A + B + C

if ans > 21:
    print("bust")
else:
    print("win")
