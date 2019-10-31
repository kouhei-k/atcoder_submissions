n = int(input())
color = [0]*(10**6+2)

for i in range(n):
    a, b = map(int, input().split())
    color[a] += 1
    color[b+1] -= 1

ans = [0]*(10**6+2)
ans[0] = color[0]
for i in range(1, 10**6+1):
    ans[i] = ans[i-1] + color[i]

print(max(ans))
