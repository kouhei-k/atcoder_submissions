S = input()
T = input()

s = len(S)
t = len(T)
ans = t
for i in range(s - t+1):
    count = 0
    for a, b in zip(S[i:], T):
        if a != b:
            count += 1
    if ans > count:
        ans = count

print(ans)
