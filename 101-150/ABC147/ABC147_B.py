S = input()
T = S[::-1]
count = 0
N = len(S)
if N % 2 == 0:
    A = int(N / 2)
else:
    A = int((N-1) / 2)

for i in range(A):
    if S[i] == T[i]:
        pass
    else:
        count += 1

print(count)
