N, M = (int(x) for x in input().split())
A = list(map(int, input().strip().split()))
A.sort(reverse=True)

for m in range(M):
    s = sum(A)
    if A[m] >= s / (4 * M):
        a = True
    else:
        a = False

if a == True:
    print("Yes")
else:
    print("No")
