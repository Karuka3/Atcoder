def main():
    A, B = (int(x) for x in input().split())
    ans = 1
    count = 0
    while ans < B:
        ans = ans - 1 + A
        count += 1
    print(count)


if __name__ == "__main__":
    main()
