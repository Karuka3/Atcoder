def main():
    S = list(input())
    T = list(input())
    k = True
    for i in range(len(S)):
        if S[i] != T[i]:
            k = False
            break
    if k:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
