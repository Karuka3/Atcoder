a, b = (int(x) for x in input().split())
result = ""
if a > b:
    for _ in range(a):
        result += str(b)
else:
    for _ in range(b):
        result += str(a)
print(result)
