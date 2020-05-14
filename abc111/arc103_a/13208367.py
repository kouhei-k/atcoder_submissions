import collections
n = int(input())
v = list(map(int, input().split()))

odd = [v[i] for i in range(n) if i % 2 == 0]
even = [v[i] for i in range(n) if i % 2 == 1]

t = collections.Counter(odd).most_common()
t2 = collections.Counter(even).most_common()


t.append([0, 0])
t2.append([0, 0])
ans = t[0][1] + t2[0][1]
if t[0][0] == t2[0][0]:
    ans = max(t[0][1] + t2[1][1], t[1][1]+t2[0][1])
print(n - ans)
