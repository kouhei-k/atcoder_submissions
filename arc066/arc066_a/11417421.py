import collections
N = int(input())
A = list(map(int, input().split()))

ans = 2**(N//2)
table = collections.defaultdict(int)
flag = True
for x in A:
    table[x] += 1

for x in table:
    if x % 2 == N % 2:
        flag = False
        break
    if x == 0 and table[x] > 1:
        flag = False
        break
    if x >= 1 and table[x] != 2:
        flag = False
        break
    if x > N - 1:
        flag = False
        break
mod = 10**9 + 7
if flag:
    print(ans % mod)
else:
    print(0)
