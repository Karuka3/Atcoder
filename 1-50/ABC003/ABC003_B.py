S = input()
T = input()
ans = True
for i in range(len(S)):
    if S[i] == T[i]:
        continue
    elif S[i] == "@" and T[i] in ["a", "t", "c", "o", "d", "e", "r"]:
        continue
    elif T[i] == "@" and S[i] in ["a", "t", "c", "o", "d", "e", "r"]:
        continue
    else:
        ans = False
        break

if ans:
    print("You can win")
else:
    print("You will lose")
