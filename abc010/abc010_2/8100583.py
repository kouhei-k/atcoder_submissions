n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(n):
    while(a[i] > 1):
        if a[i] % 2 == 0:
            a[i] -= 1
            ans += 1
            continue
        elif a[i] % 3 == 2:
            a[i] -= 1
            ans += 1
        else:
            break
print(ans)
