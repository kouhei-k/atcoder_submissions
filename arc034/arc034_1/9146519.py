N = int(input())
abcde = [list(map(int, input().split())) for i in range(N)]

score = 0
for a, b, c, d, e in abcde:
    score = max(score, a+b+c+d+(e * 110 / 900))
print(score)
