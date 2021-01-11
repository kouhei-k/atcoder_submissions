AB = list(map(int, input().split()))
if len(AB) == 1:
    AB.append(int(input()))

A = AB[0]
B = AB[1]
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
for i in range(B):
    id = i
    for x in a:
        if x == b[id]:
            id += 1
        if id >= B:
            break
    if ans < id - i:
        ans = id - i
print(ans)
