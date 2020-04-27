a, b = map(int, input().split())

d = dict()
d[0] = (0, 6)
d[1] = (3, 3)
d[2] = (2, 2)
d[3] = (2, 4)
d[4] = (1, 1)
d[5] = (1, 3)
d[6] = (1, 5)
d[7] = (0, 0)
d[8] = (0, 2)
d[9] = (0, 4)


ans = [[' ']*7 for i in range(4)]
for x in d:
    i, j = d[x]
    ans[i][j] = 'x'

A = list(map(int, input().split()))
for x in A:
    i, j = d[x]
    ans[i][j] = '.'
B = list(map(int, input().split()))
for x in B:
    i, j = d[x]
    ans[i][j] = 'o'

for i in range(4):
    print(''.join(ans[i]))
