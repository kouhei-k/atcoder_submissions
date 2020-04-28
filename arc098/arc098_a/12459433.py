N = int(input())
S = input()

L = [0]*N

l = 0
for i, x in enumerate(S):
    L[i] += l
    if x == 'E':
        l += 1
r = 0
for i, x in enumerate(S[::-1]):
    L[N-1-i] += r
    if x == 'W':
        r += 1

print(N-1 - max(L))
