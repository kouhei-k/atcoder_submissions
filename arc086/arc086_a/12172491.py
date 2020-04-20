import collections
N, K = map(int, input().split())
A = list(map(int, input().split()))

c = collections.Counter(A).most_common()


ans = 0
L = len(c)
if L >= K:
    for i in range(K, L):
        ans += c[i][1]

print(ans)
