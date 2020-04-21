N = int(input())
d = [int(x) for x in input().split()]
ans = 0
for i in range(N):
    for j in range(N):
        if i == j:
            break
        else:
            ans += d[i] * d[j]
print(ans)
