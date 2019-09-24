import collections
N = int(input())
A = list(map(int, input().split()))

table = collections.defaultdict(int)

for x in A:
    table[x] += 1

for x in table:
    if x != 0 and table[x] != 2:
        print(0)
        exit(0)

    elif N % 2 == 1:
        if x == 0 and table[x] != 1:
            print(0)
            exit(0)

    else:
        if x == 0:
            print(0)
            exit(0)

print(2**(N//2) % (10**9 + 7))
