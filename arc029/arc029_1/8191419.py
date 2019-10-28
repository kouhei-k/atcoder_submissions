N = int(input())
t = [int(input()) for i in range(N)]
t.sort(reverse=True)
nikuyaki1 = t[0]
nikuyaki2 = 0
for i in range(1, N):
    if nikuyaki1 >= nikuyaki2:
        nikuyaki2 += t[i]
    else:
        nikuyaki1 += t[i]
print(max(nikuyaki1, nikuyaki2))
