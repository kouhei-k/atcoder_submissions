N = int(input())
ans = 0
if N < 105:
    ans = 0
else:
    for i in range(105, N+1):
        if i % 2 == 1:
            count = 0
            for j in range(1, i+1):
                if i % j == 0:
                    count += 1

            if count == 8:
                ans += 1

print(ans)
