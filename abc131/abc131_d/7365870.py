N = int(input())
AB = [[0]*2 for i in range(N)]

for i in range(N):
    AB[i] = list(map(int, input().split()))

AB = sorted(AB, key=lambda x: x[1])

time = 0
for i in range(N):
    time += AB[i][0]
    if time > AB[i][1]:
        print("No")
        exit(0)

print("Yes")
