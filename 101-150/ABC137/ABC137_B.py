def main():
    K, X = (int(x) for x in input().split())
    mini = X - K + 1
    maxi = X + K
    ans = [x for x in range(mini, maxi, 1)]
    ans = " ".join(map(str, ans))
    print(ans)


if __name__ == "__main__":
    main()
