def main():
    L, R = (int(x) for x in input().split())
    if R - L > 2018:
        print(0)
    else:
        ans = 2018
        for i in range(L, R):
            for j in range(i + 1, R + 1):
                ans = min(ans, (i * j) % 2019)
        print(ans)


if __name__ == "__main__":
    main()
