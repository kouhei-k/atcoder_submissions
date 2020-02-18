s = input()
ans = 0
count = 0

for x in s.replace("BC", "Z"):
    if x == "A":
        count += 1
        continue
    elif x == "Z":
        ans += count
    else:
        count = 0
print(ans)
