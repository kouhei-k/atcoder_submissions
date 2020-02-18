N = int(input())
A = list(map(int, input().split()))
count = 0
for i in range(N):
    if A[i] % 2 == 1:
        count += 1
if count % 2 == 0:
    print("YES")
else:
    print("NO")
