import collections
N, W, K, V = map(int, input().split())
cv = [tuple(map(int, input().split())) for i in range(N)]

#ile = open('out.txt', 'w')

col = [collections.deque() for i in range(W)]
id = 0


def func(id):
    m_col = 0
    min_l = 1000
    for i in range(id):
        if len(col[i]) < min_l:
            min_l = len(col[i])
            m_col = i
    return(m_col)


idl = 0
idr = W // 2
for i in range(N):
    tmp = set()
    for j in range(W // 2):
        if col[j]:
            tmp.add(col[j][0])
    if cv[i][0] in tmp:

        col[idr].append(cv[i][0])
        # file.write(str(idr)+"
")
        print(idr)
        idr += 1
        if idr >= W:
            idr = 4
    else:
        col[idl].append(cv[i][0])
        print(idl)
        # file.write(str(idl)+"
")
        idl += 1
        if idl >= W // 2:
            idl = 0
    flag = True
    for j in range(W):
        if col[j]:
            continue
        else:
            flag = False
            break
    if flag:
        for j in range(W):
            col[j].popleft()
# for i in range(N):
#     file.write(str(i % W)+"
")
    # print(i % W)


# file.close()
