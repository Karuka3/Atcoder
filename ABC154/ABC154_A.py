S, T = input().split()
A, B = (int(x) for x in input().split())
U = input()

if S == U:
    A -= 1
elif T == U:
    B -= 1

print(str(A) + " " + str(B))
