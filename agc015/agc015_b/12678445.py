S = input()
N = len(S)
ans = N*(N-1)

for i, x in enumerate(S):
    if x == 'U':
        ans += i
    else:
        ans += N - (i+1)
print(ans)
