N, M = map(int, input().split())
a = [int(input()) for i in range(M)]
ans = 1
pos = 0


def fibonacci(N):
    prev = []
    for i in range(1, N+1):
        if i == 1 or i == 2:
            prev.append(1)
        else:
            prev.append(prev[-2] + prev[-1])
    return(prev[-1])


a.append(N + 1)

for i in range(M+1):
    dis = a[i] - pos
    if dis == 0:
        ans = 0
        break
    ans *= fibonacci(dis)
    pos = a[i]+1
print(ans % ((10**9)+7))
