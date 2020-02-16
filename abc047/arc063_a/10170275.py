S = list(input())
N = len(S)
tmp = 0
for i in range(1, N):
    if S[i] != S[i-1]:
        tmp += 1
print(tmp)
