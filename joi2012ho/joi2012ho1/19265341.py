
S = input()
N = len(S)
ans = 0
i = 0
while(i < N):
    if S[i] == 'O':
        r = 0
        while(i+r < N and S[i+r] == 'O'):
            r += 1
        tmp = r
        l = 1
        if tmp < ans:
            i += r
            continue
        while(i-l >= 0 and i+r < N and S[i-l] == 'J' and S[i+r] == 'I'):
            l += 1
            r += 1
        if tmp <= l-1 and tmp > ans:
            ans = tmp
        i += r + 1
    else:
        i += 1
print(ans)
