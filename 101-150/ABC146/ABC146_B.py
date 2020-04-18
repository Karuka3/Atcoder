N = int(input())
S = input()
res = ""
for c in S:
    m = chr((ord(c) - ord("A") + N) % 26 + ord("A"))
    res += m
print(res)
