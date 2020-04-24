N, K, Q = (int(x) for x in input().split())
A = [int(input()) for i in range(Q)]
ans = [K-Q for i in range(N)]

for a in A:
    ans[a-1] += 1

for b in ans:
    if b > 0:
        print("Yes")
    else:
        print("No")
