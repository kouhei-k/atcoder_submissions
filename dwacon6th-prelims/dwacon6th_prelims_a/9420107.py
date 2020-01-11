N = int(input())
st = [input().split() for i in range(N)]
X = input()
flag = False
ans = 0
for i in range(N):
    if flag:
        ans += int(st[i][1])
    if st[i][0] == X:
        flag = True

print(ans)
