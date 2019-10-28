import math
N = int(input())
TA = [list(map(int, input().split())) for i in range(N)]

x = 1
y = 1
for t, a in TA:
    if x <= t and y <= a:
        x = t
        y = a
    else:
        v = max(-(-x//t), -(-y//a))
        x = v * t
        y = v * a


print(x+y)
