N, a = map(int, input().split())
k = int(input())
b = list(map(int, input().split()))


K = k
if K > 10**5:
    d = dict()
    step = 0
    while(a not in d):
        d[a] = step
        a = b[a-1]
        step += 1

    c = step - d[a]
    K = k - d[a]
    K %= c


for i in range(K):
    a = b[a-1]
print(a)
