import math


def main():
    N, D = (int(x) for x in input().split())
    X = [[int(x) for x in input().split()] for i in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if distance(X[i], X[j]).is_integer():
                ans += 1
    print(ans)


def distance(y, z):
    dis = 0
    for i in range(len(y)):
        dis += (y[i] - z[i]) ** 2
    return math.sqrt(dis)


if __name__ == "__main__":
    main()
