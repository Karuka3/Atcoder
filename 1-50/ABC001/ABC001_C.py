import math


def my_round(x, d=0):
    p = 10 ** d
    return float(math.floor((x * p) + math.copysign(0.5, x))) / p


deg, dis = map(int, input().split())
deg = deg * 10
dis = my_round(dis / 60, 1)

if deg >= 1125 and deg < 3375:
    ans = "NNE"
elif deg >= 3375 and deg < 5625:
    ans = "NE"
elif deg >= 5625 and deg < 7875:
    ans = "ENE"
elif deg >= 7875 and deg < 10125:
    ans = "E"
elif deg >= 10125 and deg < 12375:
    ans = "ESE"
elif deg >= 12375 and deg < 14625:
    ans = "SE"
elif deg >= 14625 and deg < 16875:
    ans = "SSE"
elif deg >= 16875 and deg < 19125:
    ans = "S"
elif deg >= 19125 and deg < 21375:
    ans = "SSW"
elif deg >= 21375 and deg < 23625:
    ans = "SW"
elif deg >= 23625 and deg < 25875:
    ans = "WSW"
elif deg >= 25875 and deg < 28125:
    ans = "W"
elif deg >= 28125 and deg < 30375:
    ans = "WNW"
elif deg >= 30375 and deg < 32625:
    ans = "NW"
elif deg >= 32625 and deg < 34875:
    ans = "NNW"
else:
    ans = "N"

if dis >= 0 and dis <= 0.2:
    ans = "C 0"
elif dis >= 0.3 and dis <= 1.5:
    ans = ans + " 1"
elif dis >= 1.6 and dis <= 3.3:
    ans = ans + " 2"
elif dis >= 3.4 and dis <= 5.4:
    ans = ans + " 3"
elif dis >= 5.5 and dis <= 7.9:
    ans = ans + " 4"
elif dis >= 8.0 and dis <= 10.7:
    ans = ans + " 5"
elif dis >= 10.8 and dis <= 13.8:
    ans = ans + " 6"
elif dis >= 13.9 and dis <= 17.1:
    ans = ans + " 7"
elif dis >= 17.2 and dis <= 20.7:
    ans = ans + " 8"
elif dis >= 20.8 and dis <= 24.4:
    ans = ans + " 9"
elif dis >= 24.5 and dis <= 28.4:
    ans = ans + " 10"
elif dis >= 28.5 and dis <= 32.6:
    ans = ans + " 11"
else:
    ans = ans + " 12"

print(ans)
