N = int(input())
ans = (N // 10) * 100
if N % 10 > 6:
    ans += 100
else:
    ans += (N % 10)*15
print(ans)
