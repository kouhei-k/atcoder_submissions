import collections
n, k = map(int, input().split())
s = set()
A = [collections.deque() for i in range(k)]
K = k
for i in range(n):
    t = []
    a = list(map(int, input().split()))
    for j, x in enumerate(a):
        if x in s:
            continue
        else:
            A[j].append(x)
    for j in range(k):
        while(K - (n-1-i)*j >= 1 and A[j]):
            # print(K, i, j, (n-1-i)*j, K - (n-1-i)*j)
            y = A[j].popleft()
            if y in s:
                continue
            s.add(y)
            t.append(y)
            K -= 1
    t.sort()
    print(*t)
