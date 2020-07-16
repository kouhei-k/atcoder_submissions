import collections
K = int(input())

q = collections.deque()
for i in range(9):
    q.append(i+1)
while(q):
    x = q.popleft()
    k = x % 10
    for j in range(3):
        if k == 0 and j == 0:
            continue
        elif k == 9 and j == 2:
            continue
        else:
            if j == 0:
                q.append(x*10+k-1)
            elif j == 1:
                q.append(x*10 + k)
            else:
                q.append(x*10+k+1)
    #     print(q)
    # print(x)
    K -= 1
    if K == 0:
        print(x)
        break
