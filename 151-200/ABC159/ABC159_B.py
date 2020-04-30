S = input()

N = len(S)
A = S[:int((N - 1) / 2)]
B = S[int((N + 3) / 2) - 1:]

if A == B:
    if A == A[::-1] and B == B[::-1]:
        print("Yes")
    else:
        print("No")
else:
    print("No")
