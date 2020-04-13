N = int(input())
A = list(map(int, input().split()))

next = []
while(1):

    A.sort()
    m = A[0]
    next = []
    for x in A:
        if x % m:
            next.append(x % m)
    next.append(m)
    if next[0] == next[-1]:
        break
    A = list(next)
print(next[0])
