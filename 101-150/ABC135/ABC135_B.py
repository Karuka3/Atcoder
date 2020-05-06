def main():
    N = int(input())
    p = [int(x) for x in input().split()]
    count = 0
    for i, v in enumerate(p):
        if i + 1 != v:
            count += 1
    if count == 0 or count == 2:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
