def main():
    import sys
    import heapq
    input = sys.stdin.buffer.readline
    N = int(input())
    XY = [tuple(map(int, input().split())) for i in range(N)]
    M = int(input())
    OP = [list(map(int, input().split()))for i in range(M)]
    Q = int(input())
    AB = [tuple(map(int, input().split())) for i in range(Q)]
    ABI = [(AB[i][0], AB[i][1], i) for i in range(Q)]
    heapq.heapify(ABI)
    ans = [None]*Q

    def dot(A, B):
        ret = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(len(A)):
            for j in range(len(B[0])):
                ret[i][j] = A[i][0]*B[0][j] + \
                    A[i][1]*B[1][j] + A[i][2] * B[2][j]
        return(ret)
    while(ABI[0][0] == 0):
        a, b, i = heapq.heappop(ABI)
        ans[i] = (XY[b-1][0], XY[b-1][1])
    V = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    for i in range(M):
        op = OP[i]
        F = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        if op[0] == 1:
            F[0][0] = 0
            F[0][1] = 1
            F[1][0] = -1
            F[1][1] = 0
        elif op[0] == 2:
            F[0][0] = 0
            F[0][1] = -1
            F[1][0] = 1
            F[1][1] = 0
        elif op[0] == 3:
            F[0][0] = -1
            F[0][2] = op[1]*2
        else:
            F[1][1] = -1
            F[1][2] = op[1]*2

        V = dot(F, V)

        # print(F)
        # print(V)

        while(ABI and ABI[0][0] == i+1):
            a, b, id = heapq.heappop(ABI)
            b -= 1
            x, y = XY[b]
            A = [[x], [y], [1]]
            # print(A, V)
            A = dot(V, A)
            # print(A)
            ans[id] = (A[0][0], A[1][0])
    for i in range(Q):
        print(ans[i][0], ans[i][1])


main()
