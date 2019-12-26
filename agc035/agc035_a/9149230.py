import collections
N = int(input())
a = list(map(int, input().split()))
A = set()
table = collections.defaultdict(int)

for i in range(1, N):
    table[a[i]] += 1

ans = [-1]*N
ans[0] = a[0]
for i in range(1, N):
    if (a[0] ^ a[i]) in table and table[a[0] ^ a[i]] >= 1:
        if a[0] == 0:
            if table[a[i]] == 1:
                continue
        ans[1] = (a[0] ^ a[i])
        ans[2] = a[i]
        table[ans[1]] -= 1
        table[ans[2]] -= 1
        break

if ans[1] == -1:
    print("No")
    exit(0)

for i in range(3, N):
    if (ans[i-1] ^ ans[i-2]) in table and table[ans[i-1] ^ ans[i-2]] >= 1 and table[ans[i-1] ^ ans[i-2]] >= 1:

        ans[i] = ans[i-1] ^ ans[i-2]
        table[ans[i]] -= 1
    else:
        print("No")
        exit(0)
print("Yes")
