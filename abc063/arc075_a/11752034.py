N = int(input())
s = [int(input()) for i in range(N)]

S = sum(s)
if S % 10 != 0:
    print(S)
else:
    s.sort()
    ans = S
    flag = False
    for x in s:
        if x % 10 != 0:
            ans -= x
            flag = True
            break
        else:
            continue
    if flag:
        print(ans)
    else:
        print(0)
