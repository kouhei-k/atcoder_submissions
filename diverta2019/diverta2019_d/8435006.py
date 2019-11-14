N = int(input())
ans = 0
for i in range(1, int(N**0.5)+1):
    if N // i > 1:
        if i == N % (N//i - 1):
            ans += N//i - 1

print(ans)
