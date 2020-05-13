def main():
    switch_number = []
    N, M = map(int, input().split())
    for _ in range(M):
        k = tuple(map(int, input().split()))
        switch_number.append(k[1:])
    p = list(map(int, input().split()))

    ans = 0
    for i in range(2 ** N):
        binary = list(map(int, format(i, 'b').zfill(N)))
        a = True
        for k, number in enumerate(switch_number):
            count = 0
            for j in number:
                if binary[j - 1] == 1:
                    count += 1
            if count % 2 != p[k]:
                a = False
                break
        if a:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
