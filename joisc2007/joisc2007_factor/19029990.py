n = int(input())

d = dict()

for i in range(2, int(n**0.5) + 1):
    cnt = 0
    while(n and n % i == 0):
        n //= i
        cnt += 1
    if cnt:
        d[i] = cnt
if n != 1:
    d[n] = 1
ans = 0

for x in d:
    y = x
    t = y
    cnt = 0
    while(d[x] > 0):
        t = y
        while(t % x == 0 and d[x] > 0):
            d[x] -= 1
            t //= x
        y += x
        cnt += 1
    if ans < x*cnt:
        ans = x*cnt

print(ans)
