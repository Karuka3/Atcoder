def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    ans = 0
    for i in range(N):
        k = B[i] - A[i]
        if k >= 0:
            if k <= A[i + 1]:
                ans += B[i]
                A[i + 1] -= k
            else:
                ans += A[i] + A[i + 1]
                A[i + 1] = 0
        else:
            ans += B[i]

    print(ans)


if __name__ == "__main__":
    main()
