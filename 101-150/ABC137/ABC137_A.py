def main():
    A, B = (int(x) for x in input().split())
    ans = max((A - B), (A + B), A*B)
    print(ans)


if __name__ == "__main__":
    main()
