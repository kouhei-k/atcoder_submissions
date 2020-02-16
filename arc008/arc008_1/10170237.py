N = int(input())
ans = 0
if N >= 10:
    ans += (N // 10)*100
N = N % 10
if N > 6:
    ans += 100
else:
    ans += N*15

print(ans)
