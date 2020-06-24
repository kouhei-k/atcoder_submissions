S = input()
l = 0
r = len(S)

while(l < len(S) and S[l] == '_'):
    l += 1
while(r > l and S[r-1] == '_'):
    r -= 1

s = list(S[l:r].split("_"))
ans = ""
flag = True
if len(S[l:r]):
    if s[0][0].isupper():
        print(S)
        exit(0)

    for x in s:
        try:
            if x[0].isdecimal():
                flag = False
                break
        except:
            flag = False
            break
    if flag == False:
        print(S)
        exit(0)

    if len(s) == 1:
        for x in s[0]:
            if x.isupper():
                ans += '_'
                ans += x.lower()
            else:
                ans += x
    else:
        ans += s[0]
        for x in s[1:]:
            if x[0].isupper():
                flag = False
                break
            ans += x[0].upper()
            for i in range(1, len(x)):
                if x[i].isupper():
                    print(S)
                    exit(0)
                else:
                    ans += x[i]


if flag:
    for i in range(l):
        ans = "".join(["_", ans])
    for i in range(r, len(S)):
        ans = "".join([ans, "_"])

    print(ans)
else:
    print(S)
