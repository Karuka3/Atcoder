def main():
    N = int(input())
    d = [int(x) for x in input().split()]
    d.sort()
    median = int(N / 2)
    k = d[median] - d[median - 1]
    print(k)


if __name__ == "__main__":
    main()
