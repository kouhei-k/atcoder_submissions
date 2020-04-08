import fractions
N, M = map(int, input().split())
a = list(map(int, input().split()))
lcm = 1
for x in a:
    lcm = (lcm*x) // fractions.gcd(lcm, x)
ans = (M // lcm)
if M % lcm >= (lcm//2):
    ans += 1
x = a[0]
k = 0
while(x % 2 == 0):
    x = x // 2
    k += 1

for x in a[1:]:
    count = 0
    while(x % 2 == 0):
        x = x // 2
        count += 1
    if k == count:
        continue
    else:
        ans = 0


print(ans)
