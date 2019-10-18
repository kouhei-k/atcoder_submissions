N, K = map(int, input().split())
R = list(map(int, input().split()))

R.sort()

R = R[-K:]
rate = 0
for x in R:
    rate = (rate + x) / 2

print(rate)
