N = int(input())
ans = ["1", "2", "3", "4", "5", "6"]
n, p = divmod(N, 5)
s, t = divmod(n, 6)


for i in range(t):
    ans[0], ans[1], ans[2], ans[3], ans[4], ans[5] = ans[1], ans[2], ans[3], ans[4], ans[5], ans[0]

for j in range(p):
    k = j % 5
    ans[k], ans[k + 1] = ans[k + 1], ans[k]

print("".join(ans))
