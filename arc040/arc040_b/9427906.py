N, R = map(int, input().split())
S = input()
x = 0
ans = 0
k = S.rfind(".")
ans = 1
if k < 0:
    ans = 0
goal = k - (R-1)
while(x < goal):
    if S[x] == "o":
        x += 1
        ans += 1
    else:
        ans += min(R, goal-x) + 1
        x += min(R, goal - x)

print(ans)
