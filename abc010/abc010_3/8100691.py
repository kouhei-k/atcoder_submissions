tmp = list(map(int, input().split()))
t = [[tmp[0], tmp[1]], [tmp[2], tmp[3]]]
T = tmp[4]
V = tmp[5]
n = int(input())
home = [list(map(int, input().split())) for i in range(n)]


def dis(a, b, c, d):
    return (abs(c-a)**2 + abs(d-b)**2)**0.5


for i in range(n):
    tmp = 0
    d = dis(t[0][0], t[0][1], home[i][0], home[i][1])
    d += dis(home[i][0], home[i][1], t[1][0], t[1][1])
    if d <= T*V:
        print("YES")
        exit(0)
print("NO")
