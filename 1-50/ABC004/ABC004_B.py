import copy

C = [[x for x in input().split()] for _ in range(4)]
ans = copy.deepcopy(C)

for i in range(4):
    for j in range(4):
        ans[i][j] = C[3-i][3-j]

for a in ans:
    print(" ".join(a))
