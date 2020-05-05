def main():
    N = int(input())
    v = [int(x) for x in input().split()]
    while len(v) > 1:
        v.sort()
        a = v[0]
        b = v[1]
        v.pop(0)
        v.pop(0)
        new = (a + b) / 2
        v.append(new)
    print(v[0])


if __name__ == "__main__":
    main()
