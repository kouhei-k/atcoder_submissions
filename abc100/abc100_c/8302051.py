N = int(input())
a = list(map(int, input().split()))
ain2 = [0]*N
for i in range(N):
    k = a[i]
    count = 0
    while(k % 2 == 0):
        k = k / 2
        count += 1
    ain2[i] = count
print(sum(ain2))
