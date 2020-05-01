from collections import Counter


def main():
    N = int(input())
    S = [input() for _ in range(N)]
    c = Counter(S).most_common()
    ans = []
    for item in c:
        if c[0][1] == item[1]:
            ans.append(item[0])
        else:
            break
    ans.sort()

    for i in ans:
        print(i)


if __name__ == "__main__":
    main()
