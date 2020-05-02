def main():
    X = int(input())
    yen = 100
    ans = 0
    while yen < X:
        yen = int(1.01*yen)
        ans += 1
    print(ans)


if __name__ == "__main__":
    main()
