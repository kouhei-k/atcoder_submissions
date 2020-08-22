import heapq
# import collections
# from heapq import heapify
H, W, M = map(int, input().split())
hw = set([tuple(map(int, input().split())) for i in range(M)])
D1 = [0]*H
D2 = [0]*W

for x, y in hw:
    x -= 1
    y -= 1
    D1[x] += 1
    D2[y] += 1

X = max(D1)
Y = max(D2)

h = [x for x in range(H) if D1[x] == X]
w = [x for x in range(W) if D2[x] == Y]
ans = X+Y-1
for x in h:
    for y in w:
        if (x+1, y+1) not in hw:
            ans += 1
            print(ans)
            exit(0)
print(ans)
