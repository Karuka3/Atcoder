def main():
    N, L = (int(x) for x in input().split())
    azi = [L + i for i in range(N)]
    ans = sum(azi)
    if 0 not in azi:
        if azi[0] > 0:
            ans -= azi[0]
        else:
            ans -= azi[N-1]
    print(ans)


if __name__ == "__main__":
    main()
