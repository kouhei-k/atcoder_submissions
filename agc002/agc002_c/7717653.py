N, L = map(int, input().split())
a = list(map(int, input().split()))

sum = [0]*(N - 1)
for i in range(N-1):
    sum[i] = a[i] + a[i+1]

if max(sum) < L:
    print("Impossible")
else:
    print("Possible")
    id = sum.index(max(sum))
    for i in range(id):
        print(i+1)
    for i in reversed(range(id+1, N-1)):
        print(i+1)
    print(id+1)
