import numpy as np
import itertools


def main():
    N, M, X = (int(x) for x in input().split())
    A = [[int(x) for x in input().split()] for i in range(N)]
    A.sort()
    a = np.array(A)
    t = []
    ans = []
    for i in range(1, N + 1):
        C = list(itertools.combinations(A, i))
        for c in C:
            k = np.array(c)
            k = k.sum(axis=0)
            ans.append(is_ok(X, k))
    for i in ans:
        if i != -1:
            t.append(i)

    if t:
        print(min(t))
    else:
        print(-1)


def is_ok(X, k):
    M = len(k)
    f = list(map(lambda x: x >= X, k[1:M]))
    if False not in f:
        return k[0]
    else:
        return -1


if __name__ == "__main__":
    main()
