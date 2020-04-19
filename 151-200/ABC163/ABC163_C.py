from collections import Counter

N = int(input())
A = [int(x) for x in input().split()]
a = Counter(A)

for i in range(1, N + 1):
    print(a[i])
