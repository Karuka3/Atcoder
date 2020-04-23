N = int(input())
A = [int(x) for x in input().split()]
ans = sorted(range(1, N+1), key=lambda x: A[x-1])


print(" ".join(map(str, ans)))
