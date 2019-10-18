W = input()
ans = []
snatched = ["a", "i", "u", "e", "o"]
for x in W:
    if x not in snatched:
        ans.append(x)
print("".join(ans))
