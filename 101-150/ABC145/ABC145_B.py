N = int(input())
S = input()

if N % 2 == 1:
    print("No")
else:
    idx = int((N / 2))
    if S[:idx] == S[idx:]:
        print("Yes")
    else:
        print("No")
