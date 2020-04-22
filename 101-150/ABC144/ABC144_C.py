import math

N = int(input())
ans = []
k = int(math.modf(math.sqrt(N))[1])

for a in range(1, k+1):
    if N % a == 0:
        b = int(N / a)
        ans.append(a + b - 2)

print(min(ans))
