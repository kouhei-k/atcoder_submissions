N, K = map(int, input().split())
AB = [tuple(map(int, input().split())) for i in range(N)]

l = 0.0
r = 100.1
eps = 10**(-12)


def check(x):
    A = sorted([a*(b-x) for a, b in AB])
    if sum(A[-K:]) > 0:
        return(True)
    else:
        return(False)


while(l+eps < r):
    m = (l+r) / 2
    if check(m):
        l = m
    else:
        r = m
print(l)
