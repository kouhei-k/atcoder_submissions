N = int(input())
R = list(map(int, input().split()))


flag = None
ans = 1
for prev, next in zip(R[:N-1], R[1:]):
    if prev < next and (flag is None or flag):
        ans += 1
        flag = False

    elif prev > next and (flag is None or not flag):
        flag = True
        ans += 1

if ans < 3:
    ans = 0

print(ans)
