# import sys
# stdin = open('input.txt')
# input = stdin.readline
# sys.stdout = open('output.txt', 'a+')
n, k = map(int, input().split())
a = [int(input()) for i in range(n)]
S = sum(a[:k])
ans = S
for i in range(k, n):
    S -= a[i-k]
    S += a[i]
    if S > ans:
        ans = S
print(ans)
