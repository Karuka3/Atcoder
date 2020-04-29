def main():
    N, K = (int(x) for x in input().split())
    H = [int(x) for x in input().split()]
    H.sort(reverse=True)

    H = H[K:]
    print(sum(H))


if __name__ == "__main__":
    main()
