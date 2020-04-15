N = input()

for i in range(3):
    if N[i] == "7":
        a = True
        break
    else:
        a = False

if a:
    print("Yes")
else:
    print("No")
