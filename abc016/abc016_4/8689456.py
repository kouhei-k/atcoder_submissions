A = [0, 0]
B = [0, 0]
A[0], A[1], B[0], B[1] = map(int, input().split())
a = 0
b = 0


def intersect(p1, p2, p3, p4):
    tc1 = (p1[0] - p2[0]) * (p3[1] - p1[1]) + (p1[1] - p2[1]) * (p1[0] - p3[0])
    tc2 = (p1[0] - p2[0]) * (p4[1] - p1[1]) + (p1[1] - p2[1]) * (p1[0] - p4[0])
    td1 = (p3[0] - p4[0]) * (p1[1] - p3[1]) + (p3[1] - p4[1]) * (p3[0] - p1[0])
    td2 = (p3[0] - p4[0]) * (p2[1] - p3[1]) + (p3[1] - p4[1]) * (p3[0] - p2[0])
    return tc1*tc2 < 0 and td1*td2 < 0


N = int(input())
XY = [tuple(map(int, input().split())) for i in range(N)]
count = 0
prev = XY[-1]

for i, xy in enumerate(XY):
    x, y = xy
    if intersect(A, B, xy, prev):
        count += 1
    prev = [x, y]


print((count // 2) + 1)
