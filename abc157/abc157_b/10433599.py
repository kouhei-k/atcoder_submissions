A = [tuple(map(int, input().split())) for i in range(3)]
N = int(input())
b = [int(input()) for i in range(N)]
B = [[False]*3 for i in range(3)]

for x in b:
    for i in range(3):
        for j in range(3):
            if A[i][j] == x:
                B[i][j] = True
                break


flag = False
for i in range(3):
    for j in range(3):
        if B[i][j] == False:
            break
        if j == 2:
            flag = True


for j in range(3):
    for i in range(3):
        if B[i][j] == False:
            break
        if i == 2:
            flag = True

for i in range(3):
    if B[i][i] == False:
        break
    if i == 2:
        flag = True
for i in range(3):
    if B[2 - i][i] == False:
        break
    if i == 2:
        flag = True

if flag:
    print("Yes")
else:
    print("No")
