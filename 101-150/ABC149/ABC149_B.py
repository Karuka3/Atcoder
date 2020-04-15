A, B, K = (int(x) for x in input().split())

M = A + B
if K >= M:
    A = 0
    B = 0
else:
    if K >= A:
        B = B - (K - A)
        A = 0
    else:
        A = A - K

print(A, B)
