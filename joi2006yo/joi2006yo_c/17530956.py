n = int(input())
A = [1, 2, 3, 5, 4, 6]

ans = 1
for i in range(n):
    x = input()
    if x == 'East':
        A[0], A[2], A[5], A[4] = A[4], A[0], A[2], A[5]
    elif x == 'North':
        A[0], A[1], A[5], A[3] = A[1], A[5], A[3], A[0]
    elif x == 'South':
        A[0], A[3], A[5], A[1] = A[3], A[5], A[1], A[0]
    elif x == 'Left':
        A[2], A[3], A[4], A[1] = A[1], A[2], A[3], A[4]
    elif x == 'Right':
        A[4], A[1], A[2], A[3] = A[1], A[2], A[3], A[4]
    else:
        A[4], A[0], A[2], A[5] = A[0], A[2], A[5], A[4]

    ans += A[0]
print(ans)
