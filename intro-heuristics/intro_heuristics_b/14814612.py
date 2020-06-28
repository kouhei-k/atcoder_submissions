import random
D = int(input())
c = list(map(int, input().split()))
s = [list(map(int, input().split())) for i in range(D)]
t = [int(input()) for i in range(D)]

A = [0]*26

ret = 0
for i in range(D):
    ret += s[i][t[i]-1]
    # print(ret)
    A[t[i]-1] = i+1
    for j in range(26):
        ret -= c[j] * (i+1 - A[j])
    print(ret)
