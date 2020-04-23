X = int(input())
ans = 1

for j in range(10, 1, -1):
    if int(pow(X, (1/j)) + 1)**j <= X:
        ans = max(int(pow(X, (1/j))+1)**j, ans)
    else:
        ans = max(int(pow(X, (1/j)))**j, ans)

print(ans)
