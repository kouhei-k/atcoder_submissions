A, B = map(list, input().split())
A = list(map(int, A))
B = list(map(int, B))
if 9-A[0] > B[0] - 1 or(9-A[0] == B[0] - 1 and A[0] < B[0]):
    A[0] = 9
elif 9-A[0] < B[0] - 1:
    B[0] = 1
else:
    if 9-A[1] > B[1] or(9-A[1] == B[1] and A[1] < B[1]):
        A[1] = 9
    elif 9-A[1] < B[1]:
        B[1] = 0
    else:
        if 9-A[2] > B[2] or(9-A[2] == B[2] and A[2] < B[2]):
            A[2] = 9
        elif 9-A[2] < B[2]:
            B[2] = 0
A = int("".join(map(str, A)))
B = int("".join(map(str, B)))
print(A-B)
