D, N = map(int, input().split())
if N != 100:
    ans = N*(100)**D
else:
    ans = 101*(100)**D
print(ans)
