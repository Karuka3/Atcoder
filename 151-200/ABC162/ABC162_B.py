N = int(input())
sum_ = 0
for i in range(1, N+1):
    if i % 3 == 0 or i % 5 == 0:
        pass
    else:
        sum_ += i

print(sum_)