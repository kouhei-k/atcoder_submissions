N, X = map(int, input().split())
S = input()
ans = X
for x in S:
    if x == 'o':
        ans += 1
    elif ans > 0:
        ans -= 1
print(ans)
