N = int(input())
A = [int(x) for x in input().split()]
A.sort()
for i in range(1, len(A)):
    if A[i - 1] != A[i]:
        k = True
    else:
        k = False
        break

if k:
    print("YES")
else:
    print("NO")
