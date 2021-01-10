import heapq
N, C = map(int, input().split())

abc = [tuple(map(int, input().split())) for i in range(N)]

abc.sort()

X = 0
d = 0
s = 0
hq = []
flag = False

for a, b, c in abc:
    while(hq and hq[0][0] < a):
        x, y = heapq.heappop(hq)
        if flag:
            if prev == x:
                s -= y
                continue
            else:
                flag = False
        X += min(C, s)*(x-d)
        if C <= s:
            flag = True
            prev = x
        d = x
        s -= y
    X += min(C, s)*(a-d)
    d = a
    s += c
    heapq.heappush(hq, (b+1, c))
prev = 0

while(hq):
    x, y = heapq.heappop(hq)
    if flag:
        if prev == x:
            s -= y
            continue
        else:
            flag = False
    X += min(C, s)*(x-d)
    if C <= s:
        flag = True
        prev = x
    d = x
    s -= y

print(X)
