N, Q = map(int, input().split())
S = input()
lr = [tuple(map(int, input().split())) for i in range(Q)]

s = [0]*(N)
for i in range(1, N):
    s[i] = s[i-1]
    if S[i-1:i+1] == 'AC':
        s[i] += 1


for l, r in lr:
    l -= 1
    r -= 1
    if S[l] == 'C':
        print(s[r] - s[l])
    else:
        print(s[r] - s[max(0, l - 1)])
