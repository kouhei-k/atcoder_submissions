N, K = map(int, input().split())
K -= 1
ans = []
N = 2**N
while(K and K >= N // 2):
    ans.append('I'*(N//2))
    N //= 2
    K -= N
k = N // 2

ans.append('J'*(N-k) + 'O'*k)

print("".join(ans))
