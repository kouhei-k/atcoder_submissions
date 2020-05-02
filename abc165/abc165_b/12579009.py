X = int(input())
n = 100
ans = 0
while(n < X):
    ans += 1
    n *= 1.01
    n = n // 1
print(ans)
