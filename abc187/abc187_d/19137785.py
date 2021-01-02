
N = int(input())
AB = [tuple(map(int, input().split())) for i in range(N)]

AB.sort(key=lambda x: (x[0]*2 + x[1]))


SA = [0]*(N+1)
for i in range(N):
    SA[i+1] = SA[i] + AB[i][0]
B = 0
for i in range(N-1, -1, -1):
    B += AB[i][0] + AB[i][1]
    if B > SA[i]:
        print(N-i)
        exit(0)
