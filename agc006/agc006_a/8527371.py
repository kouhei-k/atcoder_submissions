import collections
N = int(input())
s = input()
t = input()
ans = list(s)
table = collections.defaultdict(int)
if s == t:
    print(N)
    exit(0)
for i in range(1, N):
    if (s + t[-i:]).endswith(t):

        print(N+i)
        exit(0)
print(2*N)
