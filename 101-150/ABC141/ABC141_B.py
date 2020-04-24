S = input()
k = False
for i, s in enumerate(S):
    if (i+1) % 2 == 0:
        if s == "L" or s == "U" or s == "D":
            k = True
        else:
            k = False
            break
    else:
        if s == "R" or s == "U" or s == "D":
            k = True
        else:
            k = False
            break

if k:
    print("Yes")
else:
    print("No")
