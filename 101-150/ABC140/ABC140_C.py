def main():
    N = int(input())
    B = [int(x) for x in input().split()]
    A = [0] * N
    A[0] = B[0]
    A[N-1] = B[-1]
    for i in range(1, N-1):
        if B[i - 1] <= B[i]:
            A[i] = B[i - 1]
        else:
            A[i] = B[i]
    print(sum(A))


if __name__ == "__main__":
    main()
