from collections import Counter
import itertools


def main():
    N, K = (int(x) for x in input().split())
    A = []
    for i in range(K):
        d = int(input())
        A.append([int(x) for x in input().split()])
    A = itertools.chain.from_iterable(A)
    p = Counter(A)
    print(N-len(p))


if __name__ == "__main__":
    main()
