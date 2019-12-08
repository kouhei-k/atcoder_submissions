S = list(input())
if len(S) % 2 == 0:
    S1 = S[:len(S)//2]
    S2 = S[len(S)//2:]
else:
    S1 = S[:len(S)//2]
    S2 = S[(len(S)//2 + 1):]

S2 = S2[::-1]
ans = 0
for i in range(len(S1)):
    if S1[i] != S2[i]:
        ans += 1
print(ans)
