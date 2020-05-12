def main():
    N = int(input())
    W = [int(x) for x in input().split()]
    w = sum(W)
    mini = w
    for i in range(N):
        a = sum(W[i+1:])
        b = w - a
        k = abs(a - b)
        if mini > k:
            mini = k
    print(mini)


if __name__ == "__main__":
    main()
