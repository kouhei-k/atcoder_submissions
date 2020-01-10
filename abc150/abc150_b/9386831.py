N = int(input())
S = list(input())

ans = 0
tmp = ""
for i in range(N):
    if tmp == 1 and S[i] == "B":
        tmp += 1
    elif tmp == 2 and S[i] == "C":
        ans += 1
        tmp = ""
    elif S[i] == "A":
        tmp = 1
    else:
        tmp = 0
print(ans)
