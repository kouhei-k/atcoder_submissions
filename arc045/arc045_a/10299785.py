S = list(input().split())
ans = []
for x in S:
    if x == "Left":
        ans.append("<")
    elif x == "Right":
        ans.append(">")
    else:
        ans.append("A")
print(" ".join(ans))
