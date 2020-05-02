def main():
    K = int(input())
    A, B = (int(x) for x in input().split())
    k = False
    for i in range(A, B + 1):
        if i % K == 0:
            k = True

    if k:
        print("OK")
    else:
        print("NG")


if __name__ == "__main__":
    main()
