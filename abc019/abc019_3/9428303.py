import collections
N = int(input())
a = list(map(int, input().split()))

table = collections.defaultdict(int)

a.sort()


for i in range(N):
    while(a[i] != 1):
        if a[i] % 2 != 0:
            break
        else:
            a[i] = a[i] // 2
    table[a[i]] += 1

print(len(table))
