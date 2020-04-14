N, L = map(int, input().split())

s = ((L+1-1) + (L+N-1))*N // 2

if L+1-1 > 0:
    print(s - (L+1-1))
else:
    if L+N-1 >= 0:
        print(s)
    else:
        print(s - (L+N-1))
