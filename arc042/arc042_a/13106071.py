N, M = map(int, input().split())

a = [int(input()) for i in range(M)]

thread = [[-i, i+1] for i in range(N)]
for i, x in enumerate(a):
    x -= 1
    thread[x][0] = i+1

thread.sort(key=lambda x: x[0], reverse=True)
ans = [thread[i][1] for i in range(N)]
print(*ans, sep='
')
