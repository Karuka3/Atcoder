def main():
    N = int(input())
    H = [int(x) for x in input().split()]
    ans = 0
    count = 0

    if N > 1:
        for i in range(1, N):
            j = i + 1
            if H[-i] <= H[-j]:
                count += 1
                if j == N:
                    if ans <= count:
                        ans = count
            else:
                if ans <= count:
                    ans = count
                count = 0
    print(ans)


if __name__ == "__main__":
    main()
