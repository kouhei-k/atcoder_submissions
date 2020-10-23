n = int(input())
m = int(input())
s = input()

c = [0]*m
flag = True
for i in range(m):
    if flag and s[i] == 'I':
        c[i] = c[i-1]+1
        flag = False
    elif flag == False and s[i] == 'O':
        c[i] = c[i-1]+1
        flag = True
    elif s[i] == 'I':
        flag = False
        c[i] = 1
    else:
        flag = True

ans = 0
for i in range(m):
    if c[i] >= 2*n+1 and c[i] % 2 == 1:
        ans += 1
#     print(ans)
# print(c)
print(ans)
