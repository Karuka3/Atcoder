def main():
    N, A, B = (int(x) for x in input().split())
    print(min([N * A, B]))


if __name__ == "__main__":
    main()
