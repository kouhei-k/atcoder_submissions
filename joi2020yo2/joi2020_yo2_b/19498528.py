N = int(input())
AT = [tuple(map(int, input().split())) for i in range(N)]
AT.sort()
T = 0
prev = 0
for a, t in AT[::-1]:
    T += abs(prev - a)
    prev = a
    if t > T:
        T = t

print(T+prev)
