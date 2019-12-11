import bisect
import sys
input = sys.stdin.readline
A, B, Q = map(int, input().split())

s = [int(input()) for i in range(A)]
t = [int(input()) for i in range(B)]

for i in range(Q):
    x = int(input())
    ret = 2 * 10**10
    a = bisect.bisect_left(s, x)
    tmp = 0
    if a < len(s):
        tmp = abs(s[a] - x)
        ab = bisect.bisect_left(t, s[a])
        if ab < len(t):
            tmp2 = abs(t[ab] - s[a])
            ret = min(ret, tmp + tmp2)

        if ab > 0:
            tmp2 = abs(t[ab - 1] - s[a])
            ret = min(ret, tmp + tmp2)
    if a > 0:
        a -= 1
        tmp = 0
        tmp = abs(s[a] - x)
        ab = bisect.bisect_left(t, s[a])
        if ab < len(t):
            tmp2 = abs(t[ab] - s[a])
            ret = min(ret, tmp + tmp2)

        if ab > 0:
            tmp2 = abs(t[ab - 1] - s[a])
            ret = min(ret, tmp + tmp2)

    b = bisect.bisect_left(t, x)
    tmp = 0
    if b < len(t):
        tmp = abs(t[b] - x)
        ba = bisect.bisect_left(s, t[b])
        if ba < len(s):
            tmp2 = abs(s[ba] - t[b])
            ret = min(ret, tmp + tmp2)
        if ba > 0:
            tmp2 = abs(s[ba - 1] - t[b])
            ret = min(ret, tmp + tmp2)
    if b > 0:
        b -= 1
        tmp = abs(t[b] - x)
        ba = bisect.bisect_left(s, t[b])
        if ba < len(s):
            tmp2 = abs(s[ba] - t[b])
            ret = min(ret, tmp + tmp2)

        if ba > 0:
            tmp2 = abs(s[ba - 1] - t[b])
            ret = min(ret, tmp + tmp2)
    print(ret)
