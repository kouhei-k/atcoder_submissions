X = int(input())
k = X % 500
ans = (X // 500)*1000
ans += (k // 5)*5

print(ans)
