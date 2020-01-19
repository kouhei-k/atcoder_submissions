import collections
N = int(input())


table = collections.defaultdict(list)

for i in range(10):
    table[i] = [0]*10


def get_initial(n):
    while(n // 10 > 0):
        n = n // 10
    return(n % 10)


for i in range(1, N+1):
    k = get_initial(i)
    table[k][i % 10] += 1
ans = 0
for i in range(1, 10):
    if i not in table:
        continue
    for j in range(1, 10):
        ans += table[i][j] * table[j][i]

print(ans)
