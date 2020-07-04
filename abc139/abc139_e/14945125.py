def main():
    import sys
    import time
    input = sys.stdin.buffer.readline
    start = time.time()
    N = int(input())
    A = [tuple(map(int, input().split())) for i in range(N)]

    id = [0]*N
    Lock = [-1]*N
    ans = 0
    min_id = 0
    M = (N*(N-1)) // 2

    while(min_id < N-1):
        now = time.time()
        if now - start > 1.9:
            ans = M
            break
        ans += 1
        if ans > M:
            break
        tmp = set()
        for i in range(N):
            if id[i] >= N-1:
                continue
            else:
                if Lock[i] >= 0:
                    continue
                else:
                    a = A[i][id[i]]
                    if Lock[a-1] == i and i not in tmp:
                        Lock[a-1] = -1
                        id[a-1] += 1
                        tmp.add(a-1)
                        id[i] += 1
                    else:
                        if i not in tmp:
                            Lock[i] = A[i][id[i]]-1
        min_id = min(id)
    if ans > M:
        print(-1)
    else:
        print(ans)


main()
