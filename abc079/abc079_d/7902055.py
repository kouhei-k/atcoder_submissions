import copy
H, W = map(int, input().split())
c = [list(map(int, input().split())) for i in range(10)]
A = [list(map(int, input().split())) for i in range(H)]
# cost = [[-1]*10 for i in range(10)]
# for j in range(10):
#     cost[j] = [[c[i][j], i] for i in range(10)]
cost = [-1]*10
cost[1] = 0

dp = [[-1]*10 for i in range(10)]
for i in range(10):
    dp[i][i] = 0


def search_cost(i, j, reached):
    # if dp[i][j] != -1:
    #     return dp[i][j]
    if cost[i] != -1:
        return cost[i]
    tmp_list = copy.copy(reached)
    tmp_list.append(i)
    ret = c[i][j]

    for k in range(10):
        if k == i or k == 1 or k in reached:
            continue
        else:
            tmp = c[i][k] + search_cost(k, j, tmp_list)
            ret = min(tmp, ret)
            if ret <= 2:
                break
            #print("i:"+str(i) + "k:" + str(k) + "j:"+str(j) + "=" + str(tmp))

    # dp[i][j] = ret
    # for i in range(10):
    #     print(dp[i])
    return ret


for i in range(10):
    if i == 1:
        continue
    else:
        if c[i][1] <= 2:
            dp[i][1] = c[i][1]
            cost[i] = c[i][1]
        else:
            cost[i] = search_cost(i, 1, [])
ans = 0
for i in range(H):
    for j in range(W):
        if A[i][j] != -1:
            ans += cost[A[i][j]]
print(ans)
