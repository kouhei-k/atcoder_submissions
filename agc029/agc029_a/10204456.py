S = input()
count = 0
ans = 0
for x in S:
    if x == "B":
        count += 1
    else:
        ans += count
print(ans)
