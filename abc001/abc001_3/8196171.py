import decimal


def round(x):
    return((x*20+1)//2/10)


Deg, Dis = map(int, input().split())
power = 0
speed = Dis / 60
speed = round(speed)
Deg_table = [1125, 3375, 5625, 7875, 10125, 12375, 14625, 16875,
             19125, 21375, 23625, 25875, 28125, 30375, 32625, 34875]
Deg_index = ["NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
             "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
Deg *= 10
Dir = "N"
for i in range(len(Deg_table)-1):
    if Deg >= Deg_table[i] and Deg_table[i+1] > Deg:
        Dir = Deg_index[i]
        break

if speed <= 0.2:
    power = 0
    Dir = "C"
elif speed <= 1.5:
    power = 1
elif speed <= 3.3:
    power = 2
elif speed <= 5.4:
    power = 3
elif speed <= 7.9:
    power = 4
elif speed <= 10.7:
    power = 5
elif speed <= 13.8:
    power = 6
elif speed <= 17.1:
    power = 7
elif speed <= 20.7:
    power = 8
elif speed <= 24.4:
    power = 9
elif speed <= 28.4:
    power = 10
elif speed <= 32.6:
    power = 11
elif speed >= 32.7:
    power = 12

print(Dir, str(power))
