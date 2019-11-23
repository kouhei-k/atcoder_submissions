import math
M = int(input())
dc = [tuple(map(int, input().split())) for i in range(M)]


def func(a, b):
    return((a+b // 10) + (a+b)-10)


num = 0
for i in range(M):
    num += dc[i][1]*9 + dc[i][1]*dc[i][0]

print(math.ceil((num-18) / 9))
