H, A = (int(x) for x in input().split())
count = 0
while H > 0:
    count += 1
    H = H - A
print(count)
