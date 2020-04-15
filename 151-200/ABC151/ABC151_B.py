N, K, M = (int(x) for x in input().split())
A = [int(x) for x in input().split()]
res = sum(A)


i = M * N - res
if i < 0:
    i = 0
if i > K:
    i = -1

print(i)
