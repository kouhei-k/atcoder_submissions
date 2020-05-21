def main():
    import heapq
    N = int(input())
    a = list(map(int, input().split()))
    q = []
    LR = [[0, N-1] for i in range(N)]
    for i in range(N):
        x = a[i]
        while(q and -q[0][0] > x):
            v, id = heapq.heappop(q)
            LR[id][1] = i - 1
        heapq.heappush(q, (-x, i))

    for i in range(N-1, -1, -1):
        x = a[i]
        while(q and -q[0][0] > x):
            v, id = heapq.heappop(q)
            LR[id][0] = i+1
        heapq.heappush(q, (-x, i))
    ans = 0
    for i in range(N):
        ans += a[i] * (LR[i][1] - i + 1)*(i - LR[i][0] + 1)
    print(ans)


main()
