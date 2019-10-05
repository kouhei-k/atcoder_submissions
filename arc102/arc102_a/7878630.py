N, K = map(int, input().split())

count = 0
count2 = 0
for i in range(1, N+1):
    if i % K == 0:
        count += 1
    elif K % 2 == 0:
        if i % K == K // 2:
            count2 += 1

ans = 0
for i in range(3):
    if i == 0:
        ans += count
        ans += count2
    elif i == 1:
        # 3C1*count*count-1
        ans += 3*count*(count-1)
        ans += 3*count2*(count2-1)
    else:
        ans += count*(count-1)*(count-2)
        ans += count2*(count2-1)*(count2-2)


print(ans)
