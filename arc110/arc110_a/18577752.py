N = int(input())
ret = 1
s = []
for i in range(2, N+1):
    s.sort()
    for x in s:
        if i % x == 0:
            i //= x
    s.append(i)
    ret *= i

print(ret + 1)
