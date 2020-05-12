def main():
    a, b = map(int, input().split())
    if a >= 13:
        ans = b
    elif a >= 6:
        ans = int(b / 2)
    else:
        ans = 0

    print(ans)


if __name__ == "__main__":
    main()
