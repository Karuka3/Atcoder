from fractions import gcd


def main():
    A, B, C, D = [int(x) for x in input().split()]
    l = (C * D) // gcd(C, D)
    b = B - anti(B, C, D, l)
    a = (A - 1) - anti((A - 1), C, D, l)
    print(int(b - a))


def anti(x, y, z, l):
    return (x // y) + (x // z) - (x // l)


if __name__ == "__main__":
    main()
