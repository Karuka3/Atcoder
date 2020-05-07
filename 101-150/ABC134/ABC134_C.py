def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    maxi = max(A)
    a = A.copy()
    a.sort()
    submaxi = max(a[:N-1])
    for i in range(N):
        if A[i] != maxi:
            print(maxi)
        else:
            print(submaxi)


if __name__ == "__main__":
    main()
