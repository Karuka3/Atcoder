import math


def main():
    A, B, H, M = map(int, input().split())
    alpha = 6 * M
    beta = (H * 30) + (M * 0.5)
    theta = math.radians(abs(alpha-beta))
    cos = math.cos(theta)
    ans = (A ** 2) + (B ** 2) - (2 * A * B * cos)
    print(math.sqrt(ans))


if __name__ == "__main__":
    main()
