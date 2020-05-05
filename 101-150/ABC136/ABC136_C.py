def main():
    N = int(input())
    H = [int(x) for x in input().split()]
    k = True
    for i in range(1, N):
        if H[i] >= H[i-1]:
            if H[i] - 1 >= H[i - 1]:
                H[i] = H[i] - 1
        else:
            k = False
            break
    if k:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
