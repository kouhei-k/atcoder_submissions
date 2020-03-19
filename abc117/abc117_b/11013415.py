N = int(input())
L = list(map(int, input().split()))
s = sum(L)
flag = True
for x in L:
    if 2*x < s:
        continue
    else:
        flag = False
        break
if flag:
    print("Yes")
else:
    print("No")
