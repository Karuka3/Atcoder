from collections import Counter

N = int(input())
S = [input() for i in range(N)]

s = Counter(S)
print(len(s))
