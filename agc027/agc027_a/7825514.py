N, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
if x == sum(a):
    print(N)
elif x > sum(a):
    print(N-1)
else:
    for i in range(N):
        if sum(a[:i+1]) > x:
            print(i)
            break
