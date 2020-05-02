def main():
    A, B, N = (int(x) for x in input().split())
    mini = 0
    if N >= B:
        ans = int(A*(B-1)/B)
    else:
        ans = int(A*(N)/B)
    print(ans)


if __name__ == "__main__":
    main()
