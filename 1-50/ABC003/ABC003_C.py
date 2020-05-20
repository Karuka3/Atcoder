N, K = map(int, input().split())
R = list(map(int, input().split()))
C = 0
R.sort(reverse=True)
ans = R[:K]
ans = ans[::-1]

for r in ans:
    C = (C + r) / 2

print(C)
