N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

diff = [A[i] - B[i] for i in range(N)]
if sum(diff) < 0:
    print(-1)
    exit(0)

minus = [diff[i] for i in range(N) if diff[i] < 0]
plus = [diff[i] for i in range(N) if diff[i] > 0]
plus.sort(reverse=True)
ans = len(minus)
minus_s = sum(minus)*(-1)
id = 0
while(minus_s > 0):
    minus_s -= plus[id]
    id += 1
print(ans+id)
