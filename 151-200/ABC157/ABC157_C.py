def main():
    N, M = (int(x) for x in input().split())
    SC = [list(map(int, input().split())) for _ in range(M)]
    for i in range(10 ** N):
        _str = str(i)
        k = True
        if len(_str) == N:
            for j in range(M):
                if _str[SC[j][0]-1] != str(SC[j][1]):
                    k = False
            if k:
                return print(i)
    return print('-1')


if __name__ == "__main__":
    main()
