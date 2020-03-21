def main():
    import collections
    H, W = map(int, input().split())
    s = [list(input()) for i in range(H)]
    t = [[0]*W for i in range(H)]
    if s[0][0] == "#":
        t[0][0] = 1

    for i in range(1, W):
        t[0][i] = t[0][i-1]
        if s[0][i] == "#" and s[0][i-1] == ".":
            t[0][i] += 1
    for i in range(1, H):
        t[i][0] = t[i-1][0]
        if s[i][0] == "#" and s[i-1][0] == ".":
            t[i][0] += 1

    for i in range(1, H):
        for j in range(1, W):
            k = 0
            l = 0
            if s[i][j] == "#":
                if s[i-1][j] != "#":
                    k += 1
                if s[i][j-1] != "#":
                    l += 1
            t[i][j] = min(t[i-1][j] + k, t[i][j-1]+l)

    print(t[-1][-1])


main()
