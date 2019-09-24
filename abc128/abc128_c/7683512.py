N, M = map(int, input().split())
k = [0]*M
s = [""]*M
for i in range(M):
    tmp = list(map(int, input().split()))
    k[i] = tmp[0]
    s[i] = tmp[1:]

p = list(map(int, input().split()))
ans = 0
for i in range(2**N):
    global_count = 0
    for j in range(M):
        local_count = 0
        for x in s[j]:
            if (i >> (x - 1)) % 2 == 0:
                continue
            else:
                local_count += 1
        if local_count % 2 == p[j]:
            global_count += 1
    if global_count == M:
        ans += 1

print(ans)
