import math
N, A, B = map(int, input().split())
H = [int(input()) for i in range(N)]
l = 0
r = math.ceil(max(H))
ans = 0
d = A-B
while(1):
    if l+1 == r:
        ans = r
        break
    else:
        m = (l+r) // 2
        count = 0
        for i in range(N):
            if (H[i] - m*B) > 0:
                count += math.ceil((H[i]-m*B) / d)
        if count <= m:
            r = m
        else:
            l = m
print(ans)
