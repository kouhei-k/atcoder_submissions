s = list(input())

i = 0
j = len(s) - 1
ans = 0
while(i <= j):
    if s[i] == s[j]:
        i += 1
        j -= 1
        continue
    else:
        if s[i] == "x":
            i += 1
            ans += 1
            continue
        elif s[j] == "x":
            j -= 1
            ans += 1
            continue
        else:
            ans = -1
            break

print(ans)
