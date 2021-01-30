N = int(input())
ans = 0
k = 0
div = []
for i in range(1, int(N**0.5)+1):
    if N % i == 0:
        div.append(i)
        if N//i != i:
            div.append(N//i)

div.sort()

for x in div:
    if x % 2 == 0:
        # if (x // 2) % 2 == 1 and (x//2)//2 > N//x:
        #     ans += 2
        continue
    else:
        k = N // x
        if k - (x//2) > 0:
            ans += 2
        y = x // 2
        if y >= k:
            ans += 2


print(ans)
