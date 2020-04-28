def main():
    N = int(input())
    X = [int(x) for x in input().split()]
    ans = []
    mini = min(X)
    maxi = max(X)
    if mini != maxi:
        for i in range(mini, maxi):
            a = map(lambda x: (x-i)**2, X)
            ans.append(sum(a))
    else:
        ans.append(0)
    return print(min(ans))


if __name__ == "__main__":
    main()
