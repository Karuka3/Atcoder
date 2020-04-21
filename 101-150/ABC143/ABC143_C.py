N = int(input())
S = input()
count = 1
for i in range(N):
    if i > 0:
        if S[i-1] != S[i]:
            count += 1

print(count)
