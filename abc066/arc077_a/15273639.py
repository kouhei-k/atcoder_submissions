import collections
n = int(input())
a = list(map(int, input().split()))
b = collections.deque()

flag = True

for x in a:
    if flag:
        b.append(x)
        flag = False
    else:
        b.appendleft(x)
        flag = True
if flag:
    print(*b)
else:
    print(*list(b)[::-1])
