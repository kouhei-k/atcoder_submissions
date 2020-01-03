N = int(input())
a = [int(input()) for i in range(N)]
count = 0
ans = ["first", "second"]
for i in range(N):
    if a[i] % 2 == 1:
        count += 1
if count > 0:
    print(ans[0])
else:
    print(ans[1])
