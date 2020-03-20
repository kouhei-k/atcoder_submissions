import collections


def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    color = [-1]*N
    G = [set() for i in range(N)]
    for i in range(N-1):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        G[u].add((v, w))
        G[v].add((u, w))
    root = 0

    color[0] = 0
    q = collections.deque()
    q.append((root, 0))
    while(q):
        x, W = q.popleft()
        for y, w in G[x]:
            if color[y] < 0:
                if (W+w) % 2 == 0:
                    color[y] = 0
                else:
                    color[y] = 1
                q.append((y, W+w))
            else:
                continue
    print(*color, sep="
")


main()
