def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    denominator = 0
    for a in A:
        denominator += 1 / a
    ans = 1 / denominator
    print(ans)


if __name__ == "__main__":
    main()
