S = input()
ans = []

prev = ""
now = ""
for i in range(len(S)):
    now = now + S[i]
    if now != prev:
        ans.append(now)
        prev = now
        now = ""


print(len(ans))
