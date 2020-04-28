ABCD = list(map(int, list(input())))
ans = ['']*9
for i in range(4):
    ans[i*2] = str(ABCD[i])
for i in range(2**3):
    ret = ABCD[0]
    for j in range(3):
        if (i >> j) % 2 == 1:
            ret += ABCD[j+1]
            ans[j*2 + 1] = '+'
        else:
            ret -= ABCD[j+1]
            ans[j*2 + 1] = '-'
    if ret == 7:
        ans[7] = '='
        ans[8] = '7'
        print(''.join(ans))
        exit(0)
