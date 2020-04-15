import collections
K = int(input())

q = collections.deque([i for i in range(1, 10)])
count = 0
while(q):
    count += 1
    x = q.popleft()
    if count == K:
        print(x)
        break
    if x % 10 != 0:
        q.append(x*10 + (x % 10 - 1))
    q.append(x*10 + (x % 10))
    if x % 10 != 9:
        q.append(x*10 + (x % 10 + 1))
