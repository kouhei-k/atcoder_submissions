N = int(input())
L = list(map(int, input().split()))
L.sort()
ans = sum([L[i] for i in range(N*2) if i % 2 == 0])
print(ans)
