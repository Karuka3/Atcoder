N = int(input())
A = list(map(int, input().strip().split()))
a = True
for i in list(filter(lambda x: x % 2 == 0, A)):
    if i % 3 != 0 and i % 5 != 0:
        print("DENIED")
        a = False
        break

if a:
    print("APPROVED")
