N = int(input())
ans = []
c = -2
if N == 0:
    ans.append('0')
while(N):
    k = N % c
    if k == c // 2:
        ans.append('1')
        N += c // 2
    else:
        ans.append('0')

    c *= -2

print(''.join(ans[::-1]))
