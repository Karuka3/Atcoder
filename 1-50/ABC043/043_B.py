s = input()
k = ""

for i in s:
    if i == "1":
        k += "1"
    elif i == "0":
        k += "0"
    else:
        _len = len(k)
        k = k[:_len-1]

print(k)
