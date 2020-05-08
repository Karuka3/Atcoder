def main():
    S = sorted(input())
    ans = "No"
    if S[0] == S[1] and S[2] == S[3] and S[0] != S[2]:
        ans = "Yes"
    print(ans)


if __name__ == "__main__":
    main()
