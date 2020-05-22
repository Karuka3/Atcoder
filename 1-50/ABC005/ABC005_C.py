T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
count = 0
ans = "no"

if M <= N:
    for b in B:
        for a in A:
            if b in list(range(a, a + T + 1)):
                count += 1
                A.remove(a)
                break
    if count == M:
        ans = "yes"

print(ans)
