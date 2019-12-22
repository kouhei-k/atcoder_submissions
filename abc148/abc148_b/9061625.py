N = int(input())
S, T = list(input().split())

ans = [""]*(N*2)
id = 0
for i in range(2*N):
    if i % 2 == 0:
        ans[i] = S[id]
    else:
        ans[i] = T[id]
        id += 1
print("".join(ans))
