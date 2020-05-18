def main():
    K = [int(input()) for _ in range(5)]
    ans = []
    A = [0]
    for k in K:
        a = k % 10
        if a == 0:
            ans.append(k)
        else:
            ans.append(k + (10 - a))
            A.append(10 - a)
    print(sum(ans) - max(A))


if __name__ == "__main__":
    main()
