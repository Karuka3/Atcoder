N, A, B = (int(x) for x in input().split())

a, b = divmod(N, (A + B))
if A <= b:
    print((a+1) * A)
else:
    print((a * A) + b)
