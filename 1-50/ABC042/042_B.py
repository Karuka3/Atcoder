N, L = (int(x) for x in input().split())
S = [input() for i in range(N)]
S = sorted(S)
s = ""

for i in range(N):
    s += S[i]

print(s)
