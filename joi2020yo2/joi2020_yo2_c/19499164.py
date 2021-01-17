def main():
    N = int(input())
    d = dict()
    ans = 1
    A = []
    for i in range(1, N):
        if i in d:
            continue
        else:
            d[i] = 0
            x = i
            count = 0
            while(x < N):
                count += 1
                for y in str(x):
                    x += int(y)
                if x in d:
                    while(d[x] != x and d[x] != 0):
                        x = d[x]

                    if d[x] == x:
                        ans += count
                        d[i] = i
                        A.append(i)
                    break
                else:
                    d[x] = i

            if x == N:
                ans += count
                d[i] = i
                A.append(i)
    print(ans)
main()
