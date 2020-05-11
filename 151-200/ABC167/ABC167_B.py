def main():
    a, b, c, k = (int(x) for x in input().split())
    ans = 0
    if k <= a:
        ans += k
    elif a + b < k and k > a:
        ans += 2 * a + b - k
    elif a + b >= k and k > a:
        ans += a

    print(ans)


if __name__ == "__main__":
    main()
