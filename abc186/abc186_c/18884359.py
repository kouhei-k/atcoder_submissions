N = int(input())
ans = N
for i in range(1, N+1):
    j = i
    while(j):
        if j % 10 == 7:
            ans -= 1
            break
        else:
            j //= 10
    if j:
        continue
    while(i):
        if i % 8 == 7:
            ans -= 1
            break
        else:
            i //= 8


print(ans)
