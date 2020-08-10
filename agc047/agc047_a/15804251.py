import collections
import sys
input = sys.stdin.readline
N = int(input())
A = [input() for i in range(N)]

C = collections.defaultdict(int)
for i, x in enumerate(A):
    idx = 0
    x = x[:-1]
    if '.' in x:
        idx = x[::-1].index('.')
        x = x.replace('.', '')
    x = int(x)
    count2 = -idx
    count5 = -idx
    while(x % 2 == 0):
        x = x // 2
        count2 += 1

    while(x % 5 == 0):
        x = x // 5
        count5 += 1
    C[(count2, count5)] += 1
ans = 0
for a, b in C:
    for a2, b2 in C:
        if a+a2 >= 0 and b+b2 >= 0:
            if a == a2 and b == b2:
                ans += C[(a, b)]*(C[(a, b)]-1)
            else:
                ans += C[(a, b)]*C[(a2, b2)]
print(ans//2)
