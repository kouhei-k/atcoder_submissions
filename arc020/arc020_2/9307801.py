import collections
n, c = map(int, input().split())
a = [int(input()) for i in range(n)]
tableOdd = collections.defaultdict(int)
tableEven = collections.defaultdict(int)
Even = n // 2
Odd = n - Even
for i in range(n):
    if i % 2 == 0:
        tableOdd[a[i]] += 1
    else:
        tableEven[a[i]] += 1

tableOdd = list(tableOdd.items())
tableOdd.sort(reverse=True,key=lambda x:x[1])
tableEven = list(tableEven.items())
tableEven.sort(reverse=True,key=lambda x:x[1])

ans = 10**9
for x, y in tableEven:
    if x != tableOdd[0][0]:
        ans = min(ans, (Even - y)*c + (Odd - tableOdd[0][1])*c)
        break
    else:
        ans = min(ans, Even*c + (Odd - tableOdd[0][1])*c)
for x, y in tableOdd:
    if x != tableEven[0][0]:
        ans = min(ans, (Odd - y)*c + (Even - tableEven[0][1])*c)
        break
    else:
        ans = min(ans, Odd*c + (Even - tableEven[0][1])*c)
print(ans)
