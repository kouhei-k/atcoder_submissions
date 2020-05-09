S = list(map(int, list(input())))
N = len(S) - 1
ans = 0
prev = 0
for i in range(2**N):
    prev = 0
    for j in range(N):
        prev *= 10
        prev += S[j]
        if (i >> j) % 2 == 1:
            ans += prev
            prev = 0
    prev *= 10
    prev += S[-1]
    ans += prev
print(ans)
