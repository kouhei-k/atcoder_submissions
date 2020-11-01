N = int(input())
ans = 0
for i in range(N):
    a, b = map(int, input().split())
    ans += (b-a+1)*(b+a) // 2
print(ans)
