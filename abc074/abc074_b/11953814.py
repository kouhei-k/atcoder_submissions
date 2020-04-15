N = int(input())
K = int(input())
x = list(map(int, input().split()))
ans = 0
for a in x:
    ans += min(a, abs(K-a))*2

print(ans)
