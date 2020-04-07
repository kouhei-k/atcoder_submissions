N, A, B = map(int, input().split())
ans = 0
for i in range(1, N+1):
    k = i
    tmp = 0
    while k > 0:
        tmp += k % 10
        k = k // 10
    if tmp >= A and tmp <= B:
        ans += i
print(ans)
