N = int(input())
k = False
for a in range(1, 10):
    for b in range(1, 10):
        if a * b == N:
            k = True
            break
if k:
    print("Yes")
else:
    print("No")
