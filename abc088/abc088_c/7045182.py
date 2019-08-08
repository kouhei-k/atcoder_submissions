c = [[]]*3

for i in range(3):
    c[i] = list(map(int, input().split()))
ans = 0
for i in range(3):
    ans += sum(c[i])

if ans % 3 == 0:
    arr = [[0]* 6]*3
    for i in range(3):
        arr[i][0] = c[i][0] - c[i][1]
        arr[i][1] = c[i][0] - c[i][2]
        arr[i][2] = c[i][1] - c[i][0]
        arr[i][3] = c[i][1] - c[i][2]
        arr[i][4] = c[i][2] - c[i][0]
        arr[i][5] = c[i][2] - c[i][1]
    for i in range(6):
        if arr[0][i] == arr[1][i] and arr[0][i] == arr[2][i]:
            continue
        else:
            print("No")
            exit(0)

    for i in range(3):
        arr[i][0] = c[0][i] - c[1][i]
        arr[i][1] = c[0][i] - c[2][i]
        arr[i][2] = c[1][i] - c[0][i]
        arr[i][3] = c[1][i] - c[2][i]
        arr[i][4] = c[2][i] - c[1][i]
        arr[i][5] = c[2][i] - c[0][i]
          

    for i in range(6):
        if arr[0][i] == arr[1][i] and arr[0][i] == arr[2][i]:
            continue
        else:
            print("No")
            exit(0)

    arr = [0]*3
    sum = 0
    for i in range(3):
        arr[0] += c[i][i]
    for i in range(3):
        if i + 1 < 3:
            arr[1] += c[i][i+1]
        else:
            arr[1] += c[i][0]
    for i in range(3):
        if i + 2 < 3:
            arr[2] += c[i][i+2]
        else:
            arr[2] += c[i][i-1]
    
    if arr[0] != arr[1] or arr[0] != arr[2]:
        print("No")
        exit(0)

    print("Yes")
    exit(0)

print("No")
