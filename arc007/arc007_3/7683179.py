c = list(input())
N = len(c)
for i in range(N):
    if c[i] == "o":
        c[i] = "1"
    else:
        c[i] = "0"

c = int("".join(c), 2)
ans = 11
for i in range(2**N):
    now = 0
    count = 0
    for j in range(N):
        if (i >> j) % 2 == 0:
            continue
        else:
            count += 1
            now |= c << j
            now |= (c << j) >> N
    if ((2**N - 1) & now) == 2**N - 1:
        ans = min(ans, count)
print(ans)
