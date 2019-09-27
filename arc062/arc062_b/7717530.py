s = input()
N = len(s)
ans = 0
count = 0
for i in range(N):
    if s[i] == "g":
        if count > 0:
            count -= 1
            ans += 1
        else:
            count += 1
    else:
        if count > 0:
            count -= 1
        else:
            count += 1
            ans -= 1

print(ans)
