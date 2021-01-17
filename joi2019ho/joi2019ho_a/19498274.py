H, W = map(int, input().split())
S = [input() for i in range(H)]

O = [0]*H
for i in range(H):
    O[i] = S[i].count("O")

I = [0]*W
for i, x in enumerate(zip(*S)):
    I[i] = x.count('I')
ans = 0
for i in range(H):
    o = O[i]
    for j in range(W):
        if S[i][j] == 'J':
            ans += o*I[j]
        elif S[i][j] == 'O':
            o -= 1
        else:
            I[j] -= 1
print(ans)
