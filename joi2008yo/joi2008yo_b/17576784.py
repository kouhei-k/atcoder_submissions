S = input()
n = len(S)
ans = 0
ans2 = 0
for i in range(n-2):
    if S[i:i+3] == 'JOI':
        ans += 1
    if S[i:i+3] == 'IOI':
        ans2 += 1
print(ans)
print(ans2)
