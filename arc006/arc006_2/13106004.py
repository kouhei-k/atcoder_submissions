N, L = map(int, input().split())

S = [input() for i in range(L+1)]

pos = S[-1].index('o')

for x in S[:-1][::-1]:
    if pos > 0 and x[pos-1] == '-':
        pos -= 2
    elif pos < 2*N - 2 and x[pos+1] == '-':
        pos += 2
print((pos+2) // 2)
