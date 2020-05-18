m = int(input())
if m < 100:
    vv = "00"
elif m >= 100 and m < 1000:
    m = int(m/100)
    vv = "0" + str(m)
elif m >= 1000 and m <= 5000:
    vv = str(int(m / 100))
elif m >= 6000 and m <= 30000:
    vv = int(m / 1000) + 50
    vv = str(vv)
elif m >= 35000 and m <= 70000:
    vv = (int(m / 1000) - 30)
    vv = int((vv/5) + 80)
    vv = str(vv)
elif m > 70000:
    vv = "89"

print(vv)
