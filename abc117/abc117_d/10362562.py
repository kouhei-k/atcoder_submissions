N, K = map(int, input().split())
A = list(map(int, input().split()))

L = len(bin(max(K, max(A)))) - 2
X = 0
ans = 0
table = [0]*L

for x in A:
    for i in range(L):
        if (x >> i) % 2 == 1:
            table[i] += 1

table = [(2**i * (N - table[i]), 2**i, table[i], table[i] > N - table[i])
         for i in range(L)]
table.sort(reverse=True)
ans = 0
tmp = 0
# print(table)
for x, y, z, flag in table:
    if flag or tmp + y > K:
        ans += (y*z)
        continue
    else:
        tmp += y
        ans += x
    #print(tmp, y, ans)
print(ans)
