N = int(input())
AB = [tuple(map(int, input().split())) for i in range(N)]


AB.sort(key=lambda x: x[1])
t = 0
for a, b in AB:
    t += a
    if t <= b:
        continue
    else:
        print("No")
        exit(0)
print("Yes")
