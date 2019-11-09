N, M = map(int, input().split())

a = [int(input()) for i in range(M)]
thread = set()
for i in reversed(range(M)):
    if a[i] not in thread:
        print(a[i])
        thread.add(a[i])
for i in range(N):
    if i+1 not in thread:
        print(i+1)
