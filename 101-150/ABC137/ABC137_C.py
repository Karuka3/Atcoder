from collections import Counter


def main():
    N = int(input())
    s = ["".join(sorted(input())) for _ in range(N)]
    S = Counter(s)
    ans = 0
    for a in S.values():
        ans += sigma(a)
    print(ans)


def sigma(x):
    sum = 0
    for i in range(1, x):
        sum += i
    return sum


if __name__ == "__main__":
    main()
