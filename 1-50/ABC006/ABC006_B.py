def tori(n):
    a, b, c = 0, 0, 1
    if n == 0:
        return a
    elif n == 1:
        return b
    elif n == 2:
        return c
    else:
        for _ in range(n - 2):
            a, b, c = b, c, (a + b + c) % 10007
    return c


if __name__ == "__main__":
    n = int(input()) - 1
    print(tori(n))
