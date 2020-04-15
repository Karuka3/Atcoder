N, K = (int(x) for x in input().split())


def base_10_to(n, b):
    if int(n / b):
        return base_10_to(int(n / b), b) + str(n % b)
    return str(n % b)


print(len(base_10_to(N, K)))
