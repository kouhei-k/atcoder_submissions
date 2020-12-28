import bisect
n = int(input())

score = [int(input()) for i in range(n)]


score2 = sorted(score)

for x in score:
    id = bisect.bisect(score2, x)
    print(n - id+1)
