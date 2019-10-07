import math
N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

diff = sum(b) - sum(a)
if diff < 0:
    print("No")
else:
    count = 0
    count2 = 0
    for i in range(N):
        if a[i] > b[i]:
            count += a[i] - b[i]
        elif a[i] < b[i]:
            count2 += math.ceil((b[i] - a[i])/2)
    if max(count, count2) > diff:
        print("No")
    else:
        print("Yes")
