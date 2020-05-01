def main():
    N = int(input())
    P = [int(x) for x in input().split()]
    count = 1
    num = P[0]
    for i in range(1, N):
        if num >= P[i]:
            count += 1
            num = P[i]
    print(count)


if __name__ == "__main__":
    main()
