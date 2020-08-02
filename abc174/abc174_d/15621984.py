N = int(input())
c = input()

l = 0
r = N-1
ans = 0
while(l < r):
    while(l < N and c[l] == 'R'):
        l += 1
    while(r >= 0 and c[r] == 'W'):
        r -= 1
    if l > r or l >= N or r < 0:
        break
    else:
        # print(l, r)
        if l-1 == r:
            ans += 1
            break
        else:
            l += 1
            r -= 1
            ans += 1

print(ans)
