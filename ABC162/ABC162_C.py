import math
from functools import reduce


def gcd(*numbers):
    return reduce(math.gcd, numbers)


K = int(input()) + 1
res = 0
for i in range(1, K):
    for j in range(1, K):
        for k in range(1, K):
            res += gcd(i, j, k)

print(res)
