N = int(input())
A = list(map(int, input().split()))
count = 0
A.sort(key=lambda x: abs(x))
for x in A:
    if x < 0:
        count += 1
A = [abs(x) for x in A]
ans = 0
if count % 2 == 0:
    ans = sum(A)
else:
    ans = sum(A[1:]) - A[0]

print(ans)
