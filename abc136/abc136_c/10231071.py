N = int(input())
H = list(map(int, input().split()))
flag = True
for i in range(N-2, -1, -1):
    if H[i+1] < H[i] - 1:
        flag = False
        break
    elif H[i+1] == H[i] - 1:
        H[i] -= 1

if flag:
    print("Yes")
else:
    print("No")
