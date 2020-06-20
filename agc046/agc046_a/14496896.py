
X = int(input())

ans = 0
x = 0
while((360-x) % X != 0):
    ans += (360 - x) // X + 1
    x = X - (360-x) % X
ans += (360-x) // X
print(ans)
