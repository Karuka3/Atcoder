N = int(input())
k = False
for a in range(1, 10):
    if N % a == 0:
        b = int(N / a)
        if b > 0 and b < 10:
            k = True
if k:
    print("Yes")
else:
    print("No")
