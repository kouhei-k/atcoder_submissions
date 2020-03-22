def main():
    H, W, K = map(int, input().split())
    S = [list(map(int, list(input()))) for i in range(H)]
    ans = (H-1)*(W-1)
    for i in range(2**(H-1)):
        border = []
        tmp = 0
        for j in range(H-1):
            if (i >> j) % 2 == 1:  # jの下に線を引く
                border.append(j)
                tmp += 1

        border.append(H-1)
        num = [0]*(tmp+1)
        flag = True
        prev = 0
        for k, x in enumerate(zip(*S)):
            sep = False
            for j, y in enumerate(border):

                if j == 0:
                    prev = 0
                else:
                    prev = border[j-1]+1

                if sep:
                    num[j] = sum(x[prev:y+1])
                elif num[j] + sum(x[prev:y+1]) > K:

                    #print(k, num[j], sum(x[prev:y+1]))
                    sep = True
                    tmp += 1
                    num[j] = sum(x[prev:y+1])
                    for l in range(j):
                        if l == 0:
                            num[l] = sum(x[:border[l]+1])
                        else:
                            num[l] = sum(x[border[l-1]:border[l]+1])
                else:
                    num[j] += sum(x[prev:y+1])

                if num[j] > K:
                    flag = False
                    break

        #print(border, tmp, flag)
        if flag:
            ans = min(ans, tmp)
        else:
            continue

    print(ans)


main()
