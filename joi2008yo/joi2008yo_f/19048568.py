def main():
    import sys
    import heapq
    input = sys.stdin.buffer.readline
    n, k = map(int, input().split())
    G = [[-1]*n for i in range(n)]
    for i in range(n):
        G[i][i] = 0
    for i in range(k):
        A = list(map(int, input().split()))
        if A[0] == 0:
            S = set()
            s = A[1] - 1
            g = A[2] - 1
            hq = [(0, s)]
            flag = True
            while(hq):
                c, x = heapq.heappop(hq)
                if x == g:
                    print(c)
                    flag = False
                    break
                else:
                    for j in range(n):
                        if j == x:
                            continue
                        elif G[x][j] == -1:
                            continue
                        else:
                            if x == s or G[s][j] == -1 or G[s][j] > c + G[x][j]:
                                G[s][j] = c + G[x][j]
                                heapq.heappush(hq, (G[s][j], j))
            if flag:
                print(-1)
        else:
            a = A[1] - 1
            b = A[2] - 1
            if G[a][b] == -1:
                G[a][b] = A[3]
            elif G[a][b] > A[3]:
                G[a][b] = A[3]
            if G[b][a] == -1:
                G[b][a] = A[3]
            elif G[b][a] > A[3]:
                G[b][a] = A[3]


main()
