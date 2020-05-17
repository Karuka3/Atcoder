def main():
    K = int(input())
    S = input()
    if K >= len(S):
        print(S)
    else:
        print(S[:K] + "...")


if __name__ == "__main__":
    main()
