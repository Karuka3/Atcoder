X, Y, Z = (int(x) for x in input().split())

X, Y = Y, X
X, Z = Z, X
print(X, Y, Z)
