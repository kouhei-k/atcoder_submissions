import collections
n = int(input())
v = list(map(int, input().split()))

odd = [v[i] for i in range(n) if i % 2 == 0]
even = [v[i] for i in range(n) if i % 2 == 1]

t = collections.defaultdict(int)
t2 = collections.defaultdict(int)
for x in odd:
    t[x] += 1
for x in even:
    t2[x] += 1

t = list(t.items())
t.sort(key = lambda x:x[1], reverse=True)

t2 = list(t2.items())
t2.sort(key = lambda x:x[1],reverse=True)


t.append([0, 0])
t2.append([0, 0])
ans = t[0][1] + t2[0][1]
if t[0][0] == t2[0][0]:
    ans = max(t[0][1] + t2[1][1], t[1][1]+t2[0][1])
print(n - ans)
