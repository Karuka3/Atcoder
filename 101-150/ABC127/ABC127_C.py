def main():
    N, M = map(int, input().split())
    L = 0
    R = N
    for _ in range(M):
        l, r = map(int, input().split())
        if L < l:
            L = l
        if R > r:
            R = r
    ans = 0
    if L <= R:
        ans = R - L + 1
    print(ans)


if __name__ == "__main__":
    main()
