def main():
    A, B = (int(x) for x in input().split())
    ans = -1
    for i in range(1009):
        if int(i * 0.08) == A and int(i * 0.1) == B:
            ans = i
            break
    print(ans)


if __name__ == "__main__":
    main()
