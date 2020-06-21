N = int(input())
a = list(map(int, input().split()))

X = 0

for x in a:
    X ^= x

ans = [X ^ a[i] for i in range(N)]

print(*ans)
