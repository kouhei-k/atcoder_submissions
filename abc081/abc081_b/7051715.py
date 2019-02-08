N = int(input())
A = list(map(int, input().split()))
flag = True
ans = 0
while(1):
    for i in range(N):
        if A[i] % 2 != 0:
            flag = False
            break
    if flag:
        A = list(map(lambda x:x/2, A))
        ans += 1
    else:
        break

print(ans)
