def main():
    import collections
    N = int(input())
    A = list(map(int, input().split()))

    table = collections.defaultdict(int)

    for x in A:
        table[x] += 1

    ret = 0
    for x in table:
        ret += (table[x]*(table[x]-1)) // 2
    for x in A:
        tmp = ret
        tmp -= (table[x]*(table[x]-1)) // 2
        tmp += ((table[x]-1)*(table[x]-2)) // 2
        print(tmp)


main()
