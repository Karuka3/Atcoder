A, B, C = (int(x) for x in input().split())
if A != B and B != C and A != C:
    print("No")
elif A == B and B == C:
    print("No")
else:
    print("Yes")
