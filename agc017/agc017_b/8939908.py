N, A, B, C, D = map(int, input().split())
if A > B:
    A, B = B, A

flag = False
diff = B-A
d = 0
for i in range(0, N, 2):
    if i > 0:
        d += D-C
    j = N-1 - i
    if diff == d and j % 2 == 0:
        flag == True
        break
    if j == 0:
        break

    k = abs(diff - d) / j
    if (k >= C and k <= D) or (abs(diff-d) >= C and abs(diff-d) <= D and j % 2 == 1):
        flag = True
        break
    k = abs(diff + d) / j
    if (k >= C and k <= D) or (diff+d >= C and diff+d <= D and j % 2 == 1):
        flag = True
        break

if flag:
    print("YES")
else:
    print("NO")
