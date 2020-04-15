import numpy as np
A1 = list(map(int, input().strip().split()))
A2 = list(map(int, input().strip().split()))
A3 = list(map(int, input().strip().split()))
N = int(input())
b = [int(input()) for i in range(N)]
A = np.array([A1, A2, A3])
K = np.empty((3, 3))

for i in range(3):
    for j in range(3):
        if A[i][j] in b:
            K[i][j] = 1
        else:
            K[i][j] = 0

if (3 in K.sum(axis=1)) or (3 in K.sum(axis=0)) or (K[0][0] == 1 and K[1][1] == 1 and K[2][2]) or (K[0][2] == 1 and K[1][1] == 1 and K[2][0]):
    print("Yes")

else:
    print("No")
