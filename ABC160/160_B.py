X = int(input())

a = divmod(X, 500)
b = divmod(a[1], 5)

print(1000*a[0] + 5*b[0])
