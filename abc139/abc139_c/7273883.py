N = int(input())

H = list(map(int, input().split()))

h = [0]*(N - 1)
for i in range(N - 1):
    h[i] = H[i+1] - H[i]

s = 0
count = [0]*(N)
prev = 0
for i in range(N-1):
    if i == 0:
        if h[0] <= 0:
            count[0] = 1
        continue
    elif h[i] <= 0:
        count[i] = count[i - 1] + 1
    else:
        count[i] = 0


print(max(count))
