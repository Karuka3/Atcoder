def main():
    N, X = (int(x) for x in input().split())
    L = [int(x) for x in input().split()]
    D = [0]

    for i in range(1, N + 1):
        a = D[i - 1] + L[i - 1]
        if a <= X:
            D.append(a)
        else:
            break

    print(len(D))


if __name__ == "__main__":
    main()
