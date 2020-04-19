N, M = (int(x) for x in input().split())
A = [int(x) for x in input().split()]

a = sum(A)
ans = N-a
if ans >= 0:
    print(ans)
else:
    print(-1)
