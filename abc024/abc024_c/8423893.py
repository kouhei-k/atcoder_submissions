N, D, K = map(int, input().split())
LR = [tuple(map(int, input().split())) for i in range(D)]
ST = [tuple(map(int, input().split())) for i in range(K)]

for s, t in ST:
    pos = s
    for i, lr in enumerate(LR):
        l, r = lr[0], lr[1]
        if pos >= l and pos <= r:
            if t >= l and t <= r:
                print(i+1)
                break
            else:
                if t < l:
                    pos = l
                else:
                    pos = r
