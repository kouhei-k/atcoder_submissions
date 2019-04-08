N = int(input())
H = list(map(int, input().split()))
flag = False
for i in reversed(range(N)):
    if flag:
        H[i] = H[i] - 1
        flag = False
    if i > 0: 
        if H[i] < H[i - 1]:
            if H[i -1] - 1 > H[i]:
                print('No')
                exit(0)
            else:
                flag = True
print('Yes')
