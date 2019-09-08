c = [[]]*3

for i in range(3):
    c[i] = list(map(int, input().split()))
ans = 0
for i in range(3):
    ans += sum(c[i])

if ans % 3 == 0:
    

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
