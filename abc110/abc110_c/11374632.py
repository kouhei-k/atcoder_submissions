def main():
    import collections
    S = input()
    T = input()
    N = len(S)
    table = collections.defaultdict(int)
    table2 = collections.defaultdict(int)
    flag = True
    for i in range(N):
        x = S[i]
        y = T[i]

        if x in table:
            if y == T[table[x]]:
                continue
            else:
                flag = False
                break
        else:
            if y in table2:
                flag = False
                break
            table[x] = i
            table2[y] = i

    if flag:
        print("Yes")
    else:
        print("No")


main()
