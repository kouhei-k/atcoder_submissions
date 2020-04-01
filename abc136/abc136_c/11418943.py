N = int(input())
H = list(map(int, input().split()))


flag = True
for i in range(1, N):
    if H[i-1] > H[i]:
        H[i] += 1
    if H[i-1] > H[i]:
        flag = False
        break
if flag:
    print("Yes")
else:
    print("No")
