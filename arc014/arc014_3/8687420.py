import collections
N = int(input())
S = list(input())

q = collections.deque()
q.append(S[0])
id = 1
ans = 1
while(id < N-1):
    if len(q) == 0:
        q.append(S[id])
        id += 1
        continue
    left = q.popleft()
    if left == S[id]:
        id += 1
        continue
    else:
        q.appendleft(left)
        right = q.pop()
        if right == S[id]:
            id += 1
            continue
        else:
            q.append(right)
            if S[id] == S[id+1]:
                id += 2
                continue
            else:
                if S[id+1] == left:
                    q.append(S[id])
                    id += 1
                else:
                    q.appendleft(S[id])
                    id += 1

if len(q) > 0 and id == N-1:
    left = q.popleft()
    if left == S[-1]:
        ans = len(q)
    else:
        q.appendleft(left)
        right = q.pop()
        if right == S[-1]:
            ans = len(q)
        else:
            ans = len(q) + 2
else:
    ans = len(q) + (N - id)
print(ans)
